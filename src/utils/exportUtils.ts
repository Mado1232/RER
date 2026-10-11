import { ExportFormat, TicketConfig } from '../types';

declare const htmlToImage: any;
declare const html2canvas: any;

export interface ExportResult {
  success: boolean;
  filename?: string;
  error?: string;
}

/**
 * Downloads a data URL as a file in the browser
 */
function triggerDownload(dataUrl: string, filename: string): void {
  const link = document.createElement('a');
  link.download = filename;
  link.href = dataUrl;
  document.body.appendChild(link);
  link.click();
  document.body.removeChild(link);
}

/**
 * Exports the ticket card element to PNG or JPG
 */
export async function exportTicketImage(
  element: HTMLElement,
  format: ExportFormat,
  config: TicketConfig
): Promise<ExportResult> {
  if (!element) {
    return { success: false, error: 'Елемент макета не знайдено' };
  }

  const cleanNumber = (config.trolleybusNumber || '334').replace(/[^a-zA-Z0-9_-]/g, '_');
  const cleanTime = (config.purchaseTime || '14-09').replace(':', '-');
  const filename = `квиток-тролейбус-№${cleanNumber}-${config.purchaseDate || '2026-09-03'}-${cleanTime}-demo.${format}`;

  try {
    // 1. Try html-to-image if available (provides razor-sharp CSS & SVG rendering)
    if (typeof htmlToImage !== 'undefined') {
      const options = {
        pixelRatio: 2.5,
        cacheBust: true,
        style: {
          transform: 'none',
          margin: '0',
        },
        backgroundColor: '#f1f5f9'
      };

      let dataUrl: string;
      if (format === 'png') {
        dataUrl = await htmlToImage.toPng(element, options);
      } else {
        dataUrl = await htmlToImage.toJpeg(element, { ...options, quality: 0.95 });
      }

      triggerDownload(dataUrl, filename);
      return { success: true, filename };
    }

    // 2. Fallback to html2canvas if htmlToImage is not loaded
    if (typeof html2canvas !== 'undefined') {
      const canvas = await html2canvas(element, {
        scale: 2.5,
        useCORS: true,
        backgroundColor: '#f1f5f9',
        logging: false
      });

      const mimeType = format === 'png' ? 'image/png' : 'image/jpeg';
      const dataUrl = canvas.toDataURL(mimeType, 0.95);
      triggerDownload(dataUrl, filename);
      return { success: true, filename };
    }

    throw new Error('Бібліотека для збереження зображення не завантажена');
  } catch (err: any) {
    console.error('Export error:', err);
    return { success: false, error: err.message || 'Не вдалося зберегти зображення' };
  }
}
