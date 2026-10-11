export const UKRAINIAN_MONTHS_GENITIVE = [
  'січня',
  'лютого',
  'березня',
  'квітня',
  'травня',
  'червня',
  'липня',
  'серпня',
  'вересня',
  'жовтня',
  'листопада',
  'грудня'
];

/**
 * Formats YYYY-MM-DD into Ukrainian readable date: e.g. "3 вересня"
 */
export function formatUkrainianDate(dateString: string): string {
  if (!dateString) return '3 вересня';
  const parts = dateString.split('-');
  if (parts.length !== 3) return '3 вересня';

  const day = parseInt(parts[2], 10);
  const monthIndex = parseInt(parts[1], 10) - 1;

  if (isNaN(day) || monthIndex < 0 || monthIndex > 11) {
    return '3 вересня';
  }

  const monthName = UKRAINIAN_MONTHS_GENITIVE[monthIndex];
  return `${day} ${monthName}`;
}

/**
 * Builds the full purchase string: "Придбано 3 вересня о 14:09"
 */
export function buildPurchaseString(dateString: string, timeString: string): string {
  const formattedDate = formatUkrainianDate(dateString);
  const cleanTime = timeString || '14:09';
  return `Придбано ${formattedDate} о ${cleanTime}`;
}

/**
 * Returns current date in YYYY-MM-DD format
 */
export function getCurrentDateString(): string {
  const now = new Date();
  const year = now.getFullYear();
  const month = String(now.getMonth() + 1).padStart(2, '0');
  const day = String(now.getDate()).padStart(2, '0');
  return `${year}-${month}-${day}`;
}

/**
 * Returns current time in HH:MM format
 */
export function getCurrentTimeString(): string {
  const now = new Date();
  const hours = String(now.getHours()).padStart(2, '0');
  const minutes = String(now.getMinutes()).padStart(2, '0');
  return `${hours}:${minutes}`;
}
