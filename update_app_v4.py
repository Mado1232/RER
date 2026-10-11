with open('app.js', 'r', encoding='utf-8') as f:
    code = f.read()

with open('qr_base64_v4.txt', 'r', encoding='utf-8') as f:
    qr_b64 = f.read().strip()

with open('cat_sticker_base64.txt', 'r', encoding='utf-8') as f:
    cat_b64 = f.read().strip()

# Replace AUTHENTIC_QR_BASE64 definition and add AUTHENTIC_CAT_STICKER_BASE64
# Find const AUTHENTIC_QR_BASE64 = ...
import re

# Look for: const AUTHENTIC_QR_BASE64 = "...";
# We can replace from `const AUTHENTIC_QR_BASE64 =` up to the next semicolon
old_qr_pattern = re.compile(r'const AUTHENTIC_QR_BASE64\s*=\s*"[^"]+";')

new_assets_code = f'''// Автентичний QR-код з правильним котиком (Retina 1:1 Base64)
  const AUTHENTIC_QR_BASE64 = "{qr_b64}";

  // Автентичний стікер котика monobank з карткою сканера (Retina Base64)
  const AUTHENTIC_CAT_STICKER_BASE64 = "{cat_b64}";'''

code, count = old_qr_pattern.subn(new_assets_code, code, count=1)
print(f'Replaced AUTHENTIC_QR_BASE64: {count}')

# Now replace TicketCard function inside app.js
# Let's inspect where TicketCard starts and ends in app.js
start_marker = '// --- Компонент квитка (TicketCard) ---'
end_marker = '// --- Панель налаштувань (ControlPanel) ---'

p_start = code.find(start_marker)
p_end = code.find(end_marker)

print(f'TicketCard positions: {p_start} to {p_end}')

new_ticket_card = '''// --- Компонент квитка (TicketCard) ---
  function TicketCard({ config, cardRef }) {
    const formattedDate = formatUkrainianDate(config.purchaseDate);
    const purchaseString = `Придбано ${formattedDate} о ${config.purchaseTime || '14:09'}`;
    const timerString = formatTimer(config.timerSeconds);
    const quoteText = config.tickerQuote || 'Життя — цікаве, і мотивація то є сильн ◆ залишайтеся людьми і кричіть, що ви живі';

    return h('div', { className: 'ticket-card-wrapper', ref: cardRef },
      // Обов'язкова позначка ЗРАЗОК / DEMO у лівому верхньому кутку
      h('div', { className: 'demo-corner-badge', title: 'Демонстраційний макет' },
        h('span', { className: 'demo-badge-dot' }),
        'ЗРАЗОК / DEMO'
      ),

      // Кнопка інформації «ⓘ» у правому верхньому кутку (на сірому фоні)
      h('button', {
        type: 'button',
        className: 'ticket-top-info-btn',
        title: 'Інформація про квиток',
        onClick: () => alert('Інформація про квиток: демонстраційний макет тролейбусного квитка.')
      }, 'i'),

      // Верхній круглий значок (фірмовий маскот-кіт monobank у рамці стікера)
      h('div', { className: 'ticket-top-emblem-container' },
        h('div', { className: 'ticket-top-emblem', title: 'monobank mascot' },
          h('img', {
            src: AUTHENTIC_CAT_STICKER_BASE64,
            className: 'ticket-sticker-img',
            alt: 'monobank cat'
          })
        )
      ),

      // ІДЕАЛЬНО БІЛЕ ТІЛО КВИТКА (Light Theme)
      h('div', { className: 'ticket-card-body' },
        // Верхня полукругла виїмка карточки під бейдж
        h('div', { className: 'ticket-notch-cutout-container' },
          h('svg', { viewBox: '0 0 106 28', className: 'ticket-notch-svg', preserveAspectRatio: 'none' },
            h('path', {
              d: 'M 0 0 L 12 0 C 20 0 26 3 31 8 C 37 16 44 24 53 24 C 62 24 69 16 75 8 C 80 3 86 0 94 0 L 106 0 Z',
              fill: '#f2f4f7'
            })
          )
        ),

        // Верхня ніжно-блакитна біжуча стрічка (Marquee)
        h('div', { className: 'ticket-ticker-strip' },
          h('div', { className: 'ticker-track' },
            h('span', { className: 'ticker-item' }, `${quoteText}   ◆   ${quoteText}   ◆  `),
            h('span', { className: 'ticker-item' }, `${quoteText}   ◆   ${quoteText}   ◆  `)
          )
        ),

        // Заголовок «Тролейбус» з тонким горизонтальним розділювачем
        h('div', { className: 'ticket-header' },
          h('h2', { className: 'ticket-title' }, 'Тролейбус'),
          h('div', { className: 'ticket-hairline' })
        ),

        // Рядок «Придбано 3 вересня о 14:09» (ненав'язливий сірий, нормальне начертання)
        h('div', { className: 'ticket-purchase-time' }, purchaseString),

        // Крупний напис «1 квиток» (системний гротеск, виразний напівжирний 700)
        h('div', { className: 'ticket-quantity' }, '1 квиток'),

        // Плашка «Квиток дійсний — 59:56» з живим таймером
        h('div', { className: 'ticket-validity-pill-wrapper' },
          h('div', { className: 'ticket-validity-pill' },
            h('span', { className: 'validity-indicator-circle' }),
            h('span', { className: 'validity-text' },
              `Квиток дійсний — ${timerString}`
            )
          )
        ),

        // Рядок «Тролейбус № 334» (слово середнє, номер напівжирний 700 з правильним знаком №)
        h('div', { className: 'ticket-transport-line' },
          h('span', { className: 'transport-label' }, 'Тролейбус'),
          h('span', { className: 'transport-number' },
            h('span', { className: 'number-sign-glyph' }, '№'),
            ` ${config.trolleybusNumber || '334'}`
          )
        ),

        // Перфорована лінія з круглими виїмками на гранях
        h('div', { className: 'ticket-perforation-container' },
          h('div', { className: 'ticket-notch notch-left' }),
          h('div', { className: 'ticket-perforation-dashed' },
            h('svg', { width: '100%', height: 2, style: { display: 'block' } },
              h('line', {
                x1: 0,
                y1: 1,
                x2: '100%',
                y2: 1,
                stroke: '#D1D5DB',
                strokeWidth: 1.5,
                strokeDasharray: '8.5 8',
                strokeLinecap: 'butt'
              })
            )
          ),
          h('div', { className: 'ticket-notch notch-right' })
        ),

        // Нижня частина з автентичним чітким QR-кодом
        h('div', { className: 'ticket-lower-section' },
          h('div', { className: 'ticket-demo-subtle-watermark' }, 'ЗРАЗОК • DEMO'),
          h('div', { className: 'ticket-qr-card' },
            h('img', {
              src: AUTHENTIC_QR_BASE64,
              alt: 'Декоративний QR-код',
              className: 'qr-image-asset',
              width: 240,
              height: 240
            })
          ),
          h('div', { className: 'ticket-id-line' },
            h('span', { className: 'ticket-id-label' }, 'Номер:'),
            h('span', { className: 'ticket-id-value' }, config.ticketNumber || '612 121')
          )
        ),

        // Волноподібний зубчастий низ
        h('div', { className: 'ticket-scalloped-bottom' },
          h('svg', {
            viewBox: '0 0 360 10',
            width: '100%',
            height: 10,
            preserveAspectRatio: 'none',
            className: 'scallop-svg'
          },
            h('path', {
              d: 'M 0 0 Q 10 10 20 0 Q 30 10 40 0 Q 50 10 60 0 Q 70 10 80 0 Q 90 10 100 0 Q 110 10 120 0 Q 130 10 140 0 Q 150 10 160 0 Q 170 10 180 0 Q 190 10 200 0 Q 210 10 220 0 Q 230 10 240 0 Q 250 10 260 0 Q 270 10 280 0 Q 290 10 300 0 Q 310 10 320 0 Q 330 10 340 0 Q 350 10 360 0 L 360 10 L 0 10 Z',
              fill: '#f2f4f7'
            })
          )
        )
      ),

      // Підпис під квитком
      h('div', { className: 'ticket-reopen-note' },
        'Ви зможете повторно відкрити цю сторінку пізніше'
      )
    );
  }

  '''

updated_code = code[:p_start] + new_ticket_card + code[p_end:]
with open('app.js', 'w', encoding='utf-8') as f:
    f.write(updated_code)

print('Successfully updated app.js with v4 TicketCard and assets')
