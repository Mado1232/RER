export interface TicketConfig {
  trolleybusNumber: string;
  purchaseDate: string; // YYYY-MM-DD
  purchaseTime: string; // HH:MM
  timerSeconds: number; // e.g. 3596 (59:56)
  isTimerRunning: boolean;
  ticketNumber: string; // e.g. "612 121"
  tickerQuote: string;  // e.g. "Життя — цікаве, і мотивація то є сильн"
  tickerTextColor?: string; // e.g. "#8c5995"
  tickerBgColor?: string;   // e.g. "#f7e9f6"
  demoMarkText: string; // "ЗРАЗОК / DEMO"
}

export type ViewMode = 'editor' | 'mobile';

export type ExportFormat = 'png' | 'jpg';
