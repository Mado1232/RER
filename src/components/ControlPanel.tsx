import React, { useState } from 'react';
import { ExportFormat, TicketConfig } from '../types';
import { getCurrentDateString, getCurrentTimeString } from '../utils/dateUtils';

interface ControlPanelProps {
  config: TicketConfig;
  onChange: (newConfig: Partial<TicketConfig>) => void;
  onReset: () => void;
  onExport: (format: ExportFormat) => void;
  isExporting: boolean;
  lang?: 'uk' | 'ru';
  onLangToggle?: () => void;
}

export const ControlPanel: React.FC<ControlPanelProps> = ({
  config,
  onChange,
  onReset,
  onExport,
  isExporting,
  lang = 'uk',
  onLangToggle
}) => {
  const [showAdvanced, setShowAdvanced] = useState(true);

  const formatTimer = (totalSeconds: number): string => {
    const mins = Math.floor(Math.max(0, totalSeconds) / 60);
    const secs = Math.max(0, totalSeconds) % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  const isUk = lang === 'uk';

  return (
    <div className="control-panel-card">
      <div className="panel-header">
        <div className="panel-title-row">
          <div className="panel-icon">
            <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z" />
            </svg>
          </div>
          <div>
            <h2 className="panel-title">{isUk ? 'Панель налаштувань' : 'Панель настроек'}</h2>
            <p className="panel-subtitle">
              {isUk ? 'Миттєве оновлення макета в реальному часі' : 'Мгновенное обновление макета в реальном времени'}
            </p>
          </div>
        </div>

        {onLangToggle && (
          <button
            type="button"
            className="lang-toggle-btn"
            onClick={onLangToggle}
            title="Змінити мову інтерфейсу"
          >
            {isUk ? 'UA ↔ RU' : 'RU ↔ UA'}
          </button>
        )}
      </div>

      <div className="panel-form">
        {/* Поле № 1 — Номер тролейбуса */}
        <div className="form-group">
          <label className="form-label" htmlFor="trolley-number-input">
            <span className="label-number">1</span>
            <span className="label-text">{isUk ? 'Номер тролейбуса' : 'Номер троллейбуса'}</span>
          </label>
          <div className="input-with-icon">
            <span className="input-badge">№</span>
            <input
              id="trolley-number-input"
              type="text"
              className="form-input"
              value={config.trolleybusNumber}
              placeholder="334"
              onChange={(e) => onChange({ trolleybusNumber: e.target.value })}
              autoComplete="off"
            />
          </div>
          <div className="quick-presets">
            <span className="presets-label">{isUk ? 'Зразки:' : 'Образцы:'}</span>
            {['334', '365', '12', '28', '502'].map((num) => (
              <button
                key={num}
                type="button"
                className={`preset-chip ${config.trolleybusNumber === num ? 'active' : ''}`}
                onClick={() => onChange({ trolleybusNumber: num })}
              >
                № {num}
              </button>
            ))}
          </div>
        </div>

        {/* Поле № 2 — Дата покупки */}
        <div className="form-group">
          <label className="form-label" htmlFor="purchase-date-input">
            <span className="label-number">2</span>
            <span className="label-text">{isUk ? 'Дата покупки' : 'Дата покупки'}</span>
          </label>
          <div className="input-calendar-wrapper">
            <input
              id="purchase-date-input"
              type="date"
              className="form-input date-input"
              value={config.purchaseDate}
              onChange={(e) => onChange({ purchaseDate: e.target.value })}
            />
          </div>
          <div className="quick-presets">
            <button
              type="button"
              className={`preset-chip ${config.purchaseDate === '2026-09-03' ? 'active' : ''}`}
              onClick={() => onChange({ purchaseDate: '2026-09-03' })}
            >
              📅 {isUk ? '3 вересня (з референсу)' : '3 сентября (из референса)'}
            </button>
            <button
              type="button"
              className="preset-chip"
              onClick={() => onChange({ purchaseDate: getCurrentDateString() })}
            >
              🗓️ {isUk ? 'Сьогодні' : 'Сегодня'}
            </button>
          </div>
        </div>

        {/* Поле № 3 — Час покупки */}
        <div className="form-group">
          <label className="form-label" htmlFor="purchase-time-input">
            <span className="label-number">3</span>
            <span className="label-text">{isUk ? 'Час покупки' : 'Время покупки'}</span>
          </label>
          <div className="input-time-wrapper">
            <input
              id="purchase-time-input"
              type="time"
              className="form-input time-input"
              value={config.purchaseTime}
              onChange={(e) => onChange({ purchaseTime: e.target.value })}
            />
          </div>
          <div className="quick-presets">
            <button
              type="button"
              className={`preset-chip ${config.purchaseTime === '14:09' ? 'active' : ''}`}
              onClick={() => onChange({ purchaseTime: '14:09' })}
            >
              🕒 14:09 (Скріншот 1)
            </button>
            <button
              type="button"
              className={`preset-chip ${config.purchaseTime === '11:29' ? 'active' : ''}`}
              onClick={() => onChange({ purchaseTime: '11:29' })}
            >
              🕒 11:29 (Скріншот 2)
            </button>
            <button
              type="button"
              className="preset-chip"
              onClick={() => onChange({ purchaseTime: getCurrentTimeString() })}
            >
              ⚡ {isUk ? 'Зараз' : 'Сейчас'}
            </button>
          </div>
        </div>

        {/* Керування «живим» таймером відліку */}
        <div className="timer-control-box">
          <div className="timer-box-header">
            <div className="timer-box-title">
              <span>⏱️</span>
              <span>{isUk ? 'Живий таймер дії:' : 'Живой таймер действия:'}</span>
            </div>
            <div className="timer-box-value">
              {formatTimer(config.timerSeconds)}
            </div>
          </div>

          <div className="timer-btn-row">
            <button
              type="button"
              className="timer-btn"
              onClick={() => onChange({ isTimerRunning: !config.isTimerRunning })}
            >
              {config.isTimerRunning ? '⏸ Пауза' : '▶ Запустити'}
            </button>
            <button
              type="button"
              className="timer-btn"
              onClick={() => onChange({ timerSeconds: 59 * 60 + 56 })}
            >
              ↺ 59:56 (Скрін 1)
            </button>
            <button
              type="button"
              className="timer-btn"
              onClick={() => onChange({ timerSeconds: 59 * 60 + 36 })}
            >
              ↺ 59:36 (Скрін 2)
            </button>
          </div>
        </div>

        {/* Додаткові параметри (Акордеон) */}
        <div className="advanced-accordion">
          <button
            type="button"
            className="accordion-toggle-btn"
            onClick={() => setShowAdvanced(!showAdvanced)}
          >
            <span>{isUk ? 'Додаткові деталі макета' : 'Дополнительные детали макета'}</span>
            <span className={`accordion-arrow ${showAdvanced ? 'open' : ''}`}>▼</span>
          </button>

          {showAdvanced && (
            <div className="accordion-content">
              <div className="form-group-sub">
                <label className="form-label-sub">{isUk ? 'Демо-номер квитка' : 'Демо-номер билета'}</label>
                <div className="sub-input-row">
                  <input
                    type="text"
                    className="form-input"
                    value={config.ticketNumber}
                    onChange={(e) => onChange({ ticketNumber: e.target.value })}
                  />
                  <button
                    type="button"
                    className="preset-chip"
                    onClick={() => onChange({ ticketNumber: '612 121' })}
                  >
                    612 121
                  </button>
                  <button
                    type="button"
                    className="preset-chip"
                    onClick={() => onChange({ ticketNumber: '250 204' })}
                  >
                    250 204
                  </button>
                </div>
              </div>

              <div className="form-group-sub">
                <label className="form-label-sub">{isUk ? 'Текст верхньої стрічки (цитата)' : 'Текст верхней полосы (цитата)'}</label>
                <input
                  type="text"
                  className="form-input"
                  value={config.tickerQuote}
                  onChange={(e) => onChange({ tickerQuote: e.target.value })}
                />
                <div className="quick-presets">
                  <button
                    type="button"
                    className="preset-chip"
                    onClick={() => onChange({ tickerQuote: '...ше — залишайтеся людьми і кричіть, що ви живі. Я >' })}
                  >
                    Цитата 1
                  </button>
                  <button
                    type="button"
                    className="preset-chip"
                    onClick={() => onChange({ tickerQuote: 'Я живий! ◆ Життя — цікаве, і мотивація то є сильн' })}
                  >
                    Цитата 2
                  </button>
                </div>
              </div>

              <div className="form-group-sub" style={{ marginTop: '12px' }}>
                <label className="form-label-sub">
                  {isUk ? 'Колір цитати (стрічки)' : 'Цвет цитаты (строки)'}
                </label>
                <div className="color-theme-chips">
                  <button
                    type="button"
                    className={`color-theme-chip ${config.tickerBgColor === '#f7e9f6' ? 'active' : ''}`}
                    onClick={() => onChange({ tickerTextColor: '#8c5995', tickerBgColor: '#f7e9f6' })}
                  >
                    <span className="color-dot" style={{ background: '#8c5995' }} />
                    Лаванда (Оригінал)
                  </button>
                  <button
                    type="button"
                    className={`color-theme-chip ${config.tickerBgColor === '#e0f2fe' ? 'active' : ''}`}
                    onClick={() => onChange({ tickerTextColor: '#0284c7', tickerBgColor: '#e0f2fe' })}
                  >
                    <span className="color-dot" style={{ background: '#0284c7' }} />
                    Блакитний
                  </button>
                  <button
                    type="button"
                    className={`color-theme-chip ${config.tickerBgColor === '#ecfdf5' ? 'active' : ''}`}
                    onClick={() => onChange({ tickerTextColor: '#059669', tickerBgColor: '#ecfdf5' })}
                  >
                    <span className="color-dot" style={{ background: '#059669' }} />
                    Смарагдовий
                  </button>
                  <button
                    type="button"
                    className={`color-theme-chip ${config.tickerBgColor === '#fdf2f8' ? 'active' : ''}`}
                    onClick={() => onChange({ tickerTextColor: '#db2777', tickerBgColor: '#fdf2f8' })}
                  >
                    <span className="color-dot" style={{ background: '#db2777' }} />
                    Рожевий
                  </button>
                  <button
                    type="button"
                    className={`color-theme-chip ${config.tickerBgColor === '#fffbeb' ? 'active' : ''}`}
                    onClick={() => onChange({ tickerTextColor: '#d97706', tickerBgColor: '#fffbeb' })}
                  >
                    <span className="color-dot" style={{ background: '#d97706' }} />
                    Бурштиновий
                  </button>
                  <button
                    type="button"
                    className={`color-theme-chip ${config.tickerBgColor === '#f3f4f6' ? 'active' : ''}`}
                    onClick={() => onChange({ tickerTextColor: '#374151', tickerBgColor: '#f3f4f6' })}
                  >
                    <span className="color-dot" style={{ background: '#374151' }} />
                    Графіт
                  </button>
                </div>
                <div className="color-picker-row">
                  <label className="color-input-item">
                    <span>{isUk ? 'Колір тексту:' : 'Цвет текста:'}</span>
                    <input
                      type="color"
                      className="color-input-bubble"
                      value={config.tickerTextColor || '#8c5995'}
                      onChange={(e) => onChange({ tickerTextColor: e.target.value })}
                    />
                  </label>
                  <label className="color-input-item">
                    <span>{isUk ? 'Колір фону:' : 'Цвет фона:'}</span>
                    <input
                      type="color"
                      className="color-input-bubble"
                      value={config.tickerBgColor || '#f7e9f6'}
                      onChange={(e) => onChange({ tickerBgColor: e.target.value })}
                    />
                  </label>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Кнопки дій */}
        <div className="action-buttons-group">
          {/* Скинути налаштування */}
          <button
            type="button"
            className="btn btn-secondary"
            onClick={onReset}
            disabled={isExporting}
          >
            <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8" />
              <path d="M3 3v5h5" />
            </svg>
            <span>{isUk ? 'Скинути налаштування' : 'Сбросить настройки'}</span>
          </button>

          {/* Завантажити PNG */}
          <button
            type="button"
            className="btn btn-primary"
            onClick={() => onExport('png')}
            disabled={isExporting}
          >
            <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            <span>{isUk ? 'Завантажити PNG' : 'Скачать PNG'}</span>
          </button>

          {/* Завантажити JPG */}
          <button
            type="button"
            className="btn btn-primary btn-jpg"
            onClick={() => onExport('jpg')}
            disabled={isExporting}
          >
            <svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" strokeWidth="2">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
              <polyline points="7 10 12 15 17 10" />
              <line x1="12" y1="15" x2="12" y2="3" />
            </svg>
            <span>{isUk ? 'Завантажити JPG' : 'Скачать JPG'}</span>
          </button>
        </div>

        {/* Застереження */}
        <div className="demo-notice-box">
          <span className="notice-icon">ℹ️</span>
          <span className="notice-text">
            {isUk
              ? 'Макет є виключно демонстраційним і містить обов’язкову позначку «ЗРАЗОК / DEMO». QR-код є декоративним і не містить платіжних даних.'
              : 'Макет является исключительно демонстрационным и содержит обязательную отметку «ЗРАЗОК / DEMO». QR-код является декоративным и не содержит платёжных данных.'}
          </span>
        </div>
      </div>
    </div>
  );
};
