import React, { useMemo } from 'react';

interface DecorativeQRProps {
  size?: number;
  className?: string;
}

export const DecorativeQR: React.FC<DecorativeQRProps> = ({ size = 200, className = '' }) => {
  const { paths, centerRect } = useMemo(() => {
    const n = 29;
    const mat: number[][] = Array.from({ length: n }, () => Array(n).fill(0));

    // Finder patterns
    const setFinder = (ox: number, oy: number) => {
      for (let r = 0; r < 7; r++) {
        for (let c = 0; c < 7; c++) {
          if (r === 0 || r === 6 || c === 0 || c === 6 || (r >= 2 && r <= 4 && c >= 2 && c <= 4)) {
            mat[oy + r][ox + c] = 1;
          } else {
            mat[oy + r][ox + c] = 0;
          }
        }
      }
    };

    setFinder(0, 0);
    setFinder(n - 7, 0);
    setFinder(0, n - 7);

    // Alignment pattern at (20, 20)
    const ax = 20;
    const ay = 20;
    for (let r = 0; r < 5; r++) {
      for (let c = 0; c < 5; c++) {
        if (r === 0 || r === 4 || c === 0 || c === 4 || (r === 2 && c === 2)) {
          mat[ay + r][ax + c] = 1;
        }
      }
    }

    // Timing lines
    for (let i = 8; i < n - 8; i++) {
      mat[6][i] = i % 2 === 0 ? 1 : 0;
      mat[i][6] = i % 2 === 0 ? 1 : 0;
    }

    // Deterministic module generation
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        // Exclude finder patterns & separators
        if ((r <= 7 && c <= 7) || (r <= 7 && c >= n - 8) || (r >= n - 8 && c <= 7)) {
          continue;
        }
        // Exclude center cutout for cat mascot (10..18)
        if (r >= 10 && r <= 18 && c >= 10 && c <= 18) {
          continue;
        }
        // Exclude alignment pattern area
        if (r >= 19 && r <= 25 && c >= 19 && c <= 25) {
          continue;
        }
        // Exclude timing lines
        if (r === 6 || c === 6) {
          continue;
        }

        const seed = (r * 37 + c * 19 + ((r * c) % 11)) % 17;
        mat[r][c] = [1, 3, 4, 7, 9, 12, 14, 15].includes(seed) ? 1 : 0;
      }
    }

    const pathList: { x: number; y: number }[] = [];
    for (let r = 0; r < n; r++) {
      for (let c = 0; c < n; c++) {
        if (mat[r][c] === 1) {
          pathList.push({ x: c, y: r });
        }
      }
    }

    return {
      paths: pathList,
      centerRect: { x: 10, y: 10, size: 9 }
    };
  }, []);

  return (
    <div className={`decorative-qr-wrapper ${className}`} style={{ width: size, height: size }}>
      <svg
        viewBox="0 0 29 29"
        width={size}
        height={size}
        style={{ display: 'block', shapeRendering: 'crispEdges' }}
      >
        {/* White background */}
        <rect width="29" height="29" fill="#ffffff" />

        {/* QR Modules */}
        {paths.map((p, idx) => (
          <rect
            key={idx}
            x={p.x}
            y={p.y}
            width="1"
            height="1"
            fill="#0f172a"
          />
        ))}

        {/* Center cutout with rounded white background */}
        <rect
          x={centerRect.x + 0.2}
          y={centerRect.y + 0.2}
          width={centerRect.size - 0.4}
          height={centerRect.size - 0.4}
          rx="1.5"
          fill="#ffffff"
        />

        {/* Cat Silhouette in the center */}
        <g transform={`translate(${centerRect.x + 4.5}, ${centerRect.y + 4.5}) scale(0.09)`}>
          <path
            d="M -22,-6 L -29,-25 C -25,-22 -19,-18 -10,-19 C -3,-20 3,-20 10,-19 C 19,-18 25,-22 29,-25 L 22,-6 C 32,4 34,18 27,30 C 20,42 3,46 -4,46 C -11,46 -28,42 -35,30 C -42,18 -40,4 -22,-6 Z"
            fill="#0f172a"
          />
        </g>
      </svg>
    </div>
  );
};
