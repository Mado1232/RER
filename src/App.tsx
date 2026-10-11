import React, { useState, useRef, useEffect } from 'react';
import { TicketConfig, ExportFormat, ViewMode } from './types';
import { ControlPanel } from './components/ControlPanel';
import { TicketCard } from './components/TicketCard';
import { exportTicketImage } from './utils/exportUtils';

const STORAGE_KEY = 'trolleybus_ticket_config_v2';
const TIMER_TARGET_KEY = 'trolleybus_ticket_timer_target_v2';

const DEFAULT_CONFIG: TicketConfig = {
  trolleybusNumber: '012',
  purchaseDate: '2026-09-07',
  purchaseTime: '09:03',
  timerSeconds: 59 * 60 + 48, // 59:48
  isTimerRunning: true,
  ticketNumber: '766 713',
  tickerQuote: 'Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі',
  tickerTextColor: '#8c5995',
  tickerBgColor: '#f7e9f6',
  demoMarkText: 'ЗРАЗОК / DEMO'
};

function loadInitialConfig(): TicketConfig {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) {
      const parsed = JSON.parse(saved);
      const merged: TicketConfig = { ...DEFAULT_CONFIG, ...parsed };
      const savedTarget = localStorage.getItem(TIMER_TARGET_KEY);
      if (savedTarget && merged.isTimerRunning) {
        const targetEpoch = parseInt(savedTarget, 10);
        if (!isNaN(targetEpoch)) {
          merged.timerSeconds = Math.max(0, Math.round((targetEpoch - Date.now()) / 1000));
        }
      }
      return merged;
    }
  } catch (e) {
    console.warn('LocalStorage load error:', e);
  }
  return DEFAULT_CONFIG;
}

export const App: React.FC = () => {
  const [config, setConfig] = useState<TicketConfig>(loadInitialConfig);
  const isCleanParam = typeof window !== 'undefined' && new URLSearchParams(window.location.search).get('view') === 'clean';
  const [viewMode, setViewMode] = useState<ViewMode>(isCleanParam ? 'mobile' : 'editor'); // 'editor' | 'mobile' (full clean view)
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const [isExporting, setIsExporting] = useState<boolean>(false);
  const [toastMessage, setToastMessage] = useState<string | null>(null);
  const [lang, setLang] = useState<'uk' | 'ru'>('uk');

  const ticketCardRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    document.title = 'pay.monobank.test';
  }, []);

  // Живий автономний таймер відліку
  useEffect(() => {
    if (!config.isTimerRunning) return;

    const syncFromTarget = () => {
      const savedTarget = localStorage.getItem(TIMER_TARGET_KEY);
      if (savedTarget) {
        const targetEpoch = parseInt(savedTarget, 10);
        if (!isNaN(targetEpoch)) {
          const remaining = Math.max(0, Math.round((targetEpoch - Date.now()) / 1000));
          setConfig((prev) => {
            if (prev.timerSeconds === remaining) return prev;
            const updated = { ...prev, timerSeconds: remaining };
            try {
              localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
            } catch (e) {}
            return updated;
          });
          return;
        }
      }
      setConfig((prev) => {
        if (prev.timerSeconds <= 0) return prev;
        const updated = { ...prev, timerSeconds: prev.timerSeconds - 1 };
        try {
          localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
        } catch (e) {}
        return updated;
      });
    };

    const timer = setInterval(syncFromTarget, 1000);

    const handleVisibilityOrFocus = () => {
      syncFromTarget();
    };

    document.addEventListener('visibilitychange', handleVisibilityOrFocus);
    window.addEventListener('pageshow', handleVisibilityOrFocus);
    window.addEventListener('focus', handleVisibilityOrFocus);

    return () => {
      clearInterval(timer);
      document.removeEventListener('visibilitychange', handleVisibilityOrFocus);
      window.removeEventListener('pageshow', handleVisibilityOrFocus);
      window.removeEventListener('focus', handleVisibilityOrFocus);
    };
  }, [config.isTimerRunning]);

  const handleConfigChange = (newValues: Partial<TicketConfig>) => {
    setConfig((prev) => {
      const nextConfig = { ...prev, ...newValues };
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(nextConfig));
        if (newValues.timerSeconds !== undefined || newValues.isTimerRunning !== undefined) {
          if (nextConfig.isTimerRunning) {
            const targetEpoch = Date.now() + nextConfig.timerSeconds * 1000;
            localStorage.setItem(TIMER_TARGET_KEY, String(targetEpoch));
          } else {
            localStorage.removeItem(TIMER_TARGET_KEY);
          }
        }
      } catch (e) {
        console.warn('LocalStorage save error:', e);
      }
      return nextConfig;
    });
  };

  const handleReset = () => {
    try {
      localStorage.removeItem(STORAGE_KEY);
      localStorage.removeItem(TIMER_TARGET_KEY);
      const targetEpoch = Date.now() + DEFAULT_CONFIG.timerSeconds * 1000;
      localStorage.setItem(TIMER_TARGET_KEY, String(targetEpoch));
      localStorage.setItem(STORAGE_KEY, JSON.stringify(DEFAULT_CONFIG));
    } catch (e) {}
    setConfig(DEFAULT_CONFIG);
    showToast(lang === 'uk' ? 'Налаштування відновлено за замовчуванням' : 'Настройки сброшены к значениям по умолчанию');
  };

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => {
      setToastMessage(null);
    }, 3800);
  };

  const handleExport = async (format: ExportFormat) => {
    const targetElement = ticketCardRef.current;
    if (!targetElement || isExporting) return;

    setIsExporting(true);
    try {
      const result = await exportTicketImage(targetElement, format, config);
      if (result.success) {
        showToast(
          lang === 'uk'
            ? `Зображення ${format.toUpperCase()} успішно завантажено!`
            : `Изображение ${format.toUpperCase()} успешно скачано!`
        );
      } else {
        showToast(result.error || 'Помилка при експорті зображення');
      }
    } catch (err: any) {
      showToast(err.message || 'Не вдалося зберегти макет');
    } finally {
      setIsExporting(false);
    }
  };

  const isUk = lang === 'uk';

  return (
    <div className="app-container">
      {/* Верхня шапка додатку */}
      <header className="app-top-header">
        <div className="app-header-content">
          <div className="app-logo">
            <span className="logo-icon">🚎</span>
            <div>
              <h1 className="app-heading">
                {isUk ? 'Редактор макета квитка' : 'Редактор макета билета'}
              </h1>
              <p className="app-subheading">
                {isUk
                  ? 'Інтерактивний живий перегляд тролейбусного квитка у світлій темі'
                  : 'Интерактивный живой просмотр троллейбусного билета в светлой теме'}
              </p>
            </div>
          </div>

          <div className="header-controls">
            {/* Перемикач режимів: Редактор / Повний вигляд квитка */}
            <div className="mode-switch-group">
              <button
                type="button"
                className={`mode-btn ${viewMode === 'editor' ? 'active' : ''}`}
                onClick={() => setViewMode('editor')}
              >
                🛠️ {isUk ? 'Режим редактора' : 'Режим редактора'}
              </button>
              <button
                type="button"
                className={`mode-btn ${viewMode === 'mobile' ? 'active' : ''}`}
                onClick={() => setViewMode('mobile')}
              >
                👁️ {isUk ? 'Чистий вигляд квитка' : 'Чистый вид билета'}
              </button>
            </div>

            <span className="badge-demo-status">
              🛡️ ЗРАЗОК / DEMO
            </span>
          </div>
        </div>
      </header>

      {/* --- РЕЖИМ 1: РЕДАКТОР (Двоколонковий адаптивний) --- */}
      {viewMode === 'editor' && (
        <main className="app-main-layout">
          {/* Ліва колонка: Налаштування */}
          <section className="settings-section">
            <ControlPanel
              config={config}
              onChange={handleConfigChange}
              onReset={handleReset}
              onExport={handleExport}
              isExporting={isExporting}
              lang={lang}
              onLangToggle={() => setLang(lang === 'uk' ? 'ru' : 'uk')}
            />
          </section>

          {/* Права колонка: Живий попередній перегляд */}
          <section className="preview-section">
            <div className="preview-card-container">
              <div className="preview-badge-header">
                <span className="preview-live-indicator"></span>
                <span className="preview-label">
                  {isUk ? 'Живий перегляд у реальному часі' : 'Живой просмотр в реальном времени'}
                </span>
              </div>

              {/* Сама карточка квитка на чистій світлій підкладці */}
              <div className="ticket-export-wrapper" id="ticket-export-target">
                <TicketCard
                  config={config}
                  cardRef={ticketCardRef}
                  showWatermark={true}
                />
              </div>
            </div>
          </section>
        </main>
      )}

      {/* --- РЕЖИМ 2: ЧИСТИЙ ПОВНОЕКРАННИЙ ВИГЛЯД (КІНЦЕВИЙ РЕЗУЛЬТАТ БЕЗ ЗАЙВИХ КНОПОК) --- */}
      {viewMode === 'mobile' && (
        <div className="clean-ticket-view-wrapper">
          <div className="ticket-export-wrapper" id="ticket-export-target">
            <TicketCard
              config={config}
              cardRef={ticketCardRef}
              showWatermark={false}
              onBackToEditor={() => setViewMode('editor')}
            />
          </div>
        </div>
      )}

      {/* Toast сповіщення */}
      {toastMessage && (
        <div className="app-toast">
          <span className="toast-icon">✓</span>
          <span className="toast-text">{toastMessage}</span>
        </div>
      )}
    </div>
  );
};
