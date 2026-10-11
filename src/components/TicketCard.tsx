import React from 'react';
import { TicketConfig } from '../types';
import { buildPurchaseString } from '../utils/dateUtils';
import { AUTHENTIC_QR_BASE64 } from '../assets/qrAsset';
import { AUTHENTIC_CAT_STICKER_BASE64 } from '../assets/catAsset';

interface TicketCardProps {
  config: TicketConfig;
  cardRef?: React.RefObject<HTMLDivElement>;
  showWatermark?: boolean;
  onBackToEditor?: () => void;
}

export const TicketCard: React.FC<TicketCardProps> = ({
  config,
  cardRef,
  showWatermark = true,
  onBackToEditor
}) => {
  const purchaseLine = buildPurchaseString(config.purchaseDate, config.purchaseTime);

  // Форматування секунд у MM:SS
  const formatTimer = (totalSeconds: number): string => {
    const mins = Math.floor(Math.max(0, totalSeconds) / 60);
    const secs = Math.max(0, totalSeconds) % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  };

  const timerText = formatTimer(config.timerSeconds);
  const quoteText = config.tickerQuote || 'Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі';

  return (
    <div className="ticket-card-wrapper" ref={cardRef}>
      {/* Обов'язкова позначка ЗРАЗОК / DEMO у верхньому лівому кутку (тільки якщо showWatermark = true) */}
      {showWatermark && (
        <div className="demo-corner-badge" title="Демонстраційний зразок">
          <span className="demo-badge-dot"></span>
          ЗРАЗОК / DEMO
        </div>
      )}

      {/* Кнопка інформації «ⓘ» у верхньому правому кутку */}
      <button
        type="button"
        className="ticket-top-info-btn"
        title="Інформація про квиток"
        onClick={() => {
          if (!showWatermark && onBackToEditor) {
            if (confirm('Повернутися до редактора налаштувань?')) {
              onBackToEditor();
            }
          } else {
            alert('Інформація про квиток: демонстраційний макет тролейбусного квитка.');
          }
        }}
      >
        i
      </button>

      {/* Верхній круглий значок (фірмовий маскот-кіт monobank у круглій рамці) */}
      <div className="ticket-top-emblem-container">
        <div className="ticket-top-notch-bg">
          <svg viewBox="0 0 110 52" className="notch-svg-curve" preserveAspectRatio="none">
            <path d="M 0,0 C 18,0 24,46 55,46 C 86,46 92,0 110,0 Z" fill="#f2f4f7" />
          </svg>
        </div>
        <div className="ticket-emblem-circle" title="Фірмовий маскот monobank">
          <img
            src={AUTHENTIC_CAT_STICKER_BASE64}
            alt="Маскот monobank"
            className="cat-sticker-image"
          />
        </div>
      </div>

      {/* Основна біла картка квитка */}
      <div className="ticket-card-body">
        {/* Верхня біжуча стрічка з підтримкою кастомних кольорів */}
        <div
          className="ticket-ticker-strip"
          style={{ background: config.tickerBgColor || '#f7e9f6' }}
        >
          <div className="ticker-track">
            <span
              className="ticker-item"
              style={{ color: config.tickerTextColor || '#8c5995' }}
            >
              {quoteText}   ◆   {quoteText}   ◆  
            </span>
            <span
              className="ticker-item"
              style={{ color: config.tickerTextColor || '#8c5995' }}
            >
              {quoteText}   ◆   {quoteText}   ◆  
            </span>
          </div>
        </div>

        {/* Заголовок «Тролейбус» з тонкою розділовою лінією */}
        <div className="ticket-header">
          <h2 className="ticket-title">Тролейбус</h2>
          <div className="ticket-hairline"></div>
        </div>

        {/* Рядок «Придбано 3 вересня о 14:09» */}
        <div className="ticket-purchase-time">{purchaseLine}</div>

        {/* Крупний напис «1 квиток» з автентичною одиницею за наданим референсом */}
        <div className="ticket-quantity">
          <span className="digit-one-svg-wrapper">
            <svg
              viewBox="0 0 27 46"
              className="digit-one-svg"
              aria-hidden="true"
              focusable="false"
            >
              <polygon points="13.3,0 18.3,0 18.3,39.5 26.6,39.5 26.6,44.5 2.4,44.5 2.4,39.5 12.0,39.5 12.0,11.0 3.0,16.5 0.5,14.0 0.5,11.5" />
            </svg>
          </span>
          <span className="ticket-quantity-word">квиток</span>
        </div>

        {/* Плашка «Квиток дійсний — MM:SS» */}
        <div className="ticket-validity-pill-wrapper">
          <div className="ticket-validity-pill">
            <span className="validity-indicator-circle"></span>
            <span className="validity-text">Квиток дійсний — {timerText}</span>
          </div>
        </div>

        {/* Номер тролейбуса */}
        <div className="ticket-transport-line">
          <span className="transport-label">Тролейбус</span>
          <span className="transport-number">
            <span className="number-sign-glyph">№</span>
            {` ${config.trolleybusNumber || '334'}`}
          </span>
        </div>

        {/* Перфорована лінія відриву */}
        <div className="ticket-perforation-container">
          <div className="ticket-notch notch-left"></div>
          <div className="ticket-perforation-dashed">
            <svg width="100%" height={2} style={{ display: 'block' }}>
              <line
                x1={0}
                y1={1}
                x2="100%"
                y2={1}
                stroke="#D1D5DB"
                strokeWidth={1.5}
                strokeDasharray="8.5 8"
                strokeLinecap="butt"
              />
            </svg>
          </div>
          <div className="ticket-notch notch-right"></div>
        </div>

        {/* Нижня частина з автентичним QR-кодом */}
        <div className="ticket-lower-section">
          {showWatermark && <div className="ticket-demo-subtle-watermark">ЗРАЗОК • DEMO</div>}
          <div className="ticket-qr-card">
            <img
              src={AUTHENTIC_QR_BASE64}
              alt="Декоративний QR-код"
              className="qr-image-asset"
              width={240}
              height={240}
            />
          </div>
          <div className="ticket-id-line">
            <span className="ticket-id-label">Номер:</span>
            <span className="ticket-id-value">{config.ticketNumber || '612 121'}</span>
          </div>
        </div>

        {/* Хвилеподібний плавний низ за референсом monobank */}
        <div className="ticket-scalloped-bottom">
          <svg viewBox="0 0 420 24" width="100%" height={24} preserveAspectRatio="none" className="scallop-svg">
            <path
              d="M 0 0 L 0 12 Q 17.0 22, 34.0 12 Q 51.0 2, 68.0 12 Q 85.0 22, 102.0 12 Q 119.0 2, 136.0 12 Q 153.0 22, 170.0 12 Q 187.0 2, 204.0 12 Q 221.0 22, 238.0 12 Q 255.0 2, 272.0 12 Q 289.0 22, 306.0 12 Q 323.0 2, 340.0 12 Q 357.0 22, 374.0 12 Q 391.0 2, 408.0 12 Q 425.0 22, 420.0 12 L 420 0 Z"
              fill="#ffffff"
            />
          </svg>
        </div>
      </div>

      {/* Підпис під квитком */}
      <div className="ticket-reopen-note">
        Ви зможете повторно відкрити цю сторінку пізніше
      </div>
    </div>
  );
};