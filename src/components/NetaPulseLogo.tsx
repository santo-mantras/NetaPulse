import React from 'react';
import { motion } from 'framer-motion';

interface NetaPulseLogoProps {
  className?: string;
  size?: number;
}

export const NetaPulseLogo: React.FC<NetaPulseLogoProps> = ({ className = "w-10 h-10" }) => {
  return (
    <div className={`relative flex items-center justify-center ${className}`}>
      {/* Dynamic Ambient Glow Ring */}
      <motion.div
        animate={{
          scale: [1, 1.25, 1],
          opacity: [0.35, 0.75, 0.35]
        }}
        transition={{
          repeat: Infinity,
          duration: 2.2,
          ease: "easeInOut"
        }}
        className="absolute inset-0 rounded-2xl bg-gradient-to-tr from-blue-600 via-indigo-500 to-purple-600 blur-sm -z-10"
      />

      {/* Main Beating SVG Badge */}
      <motion.svg
        viewBox="0 0 200 200"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        animate={{ scale: [1, 1.06, 1, 1.06, 1] }}
        transition={{ repeat: Infinity, duration: 2.2, ease: "easeInOut" }}
        className="w-full h-full drop-shadow-md"
      >
        <defs>
          <linearGradient id="npPulseGrad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" stopColor="#1E40AF" />
            <stop offset="50%" stopColor="#4338CA" />
            <stop offset="100%" stopColor="#6D28D9" />
          </linearGradient>
          <filter id="npGlow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feMerge>
              <feMergeNode in="blur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
        </defs>

        {/* Shield / Badge Frame */}
        <rect x="16" y="16" width="168" height="168" rx="44" fill="url(#npPulseGrad)" />
        <rect x="22" y="22" width="156" height="156" rx="38" stroke="white" strokeOpacity="0.3" strokeWidth="2.5" fill="none" />

        {/* Tricolor Saffron Top Arc */}
        <path d="M 42 42 Q 100 24 158 42" stroke="#FF9933" strokeWidth="4" strokeLinecap="round" fill="none" opacity="0.95" />

        {/* Civic Pulse Grid Rings */}
        <circle cx="100" cy="104" r="44" stroke="white" strokeOpacity="0.12" strokeWidth="1.5" strokeDasharray="4 4" fill="none" />
        <circle cx="100" cy="104" r="22" stroke="white" strokeOpacity="0.15" strokeWidth="1.5" fill="none" />

        {/* Ghost Path */}
        <path
          d="M 34 104 L 66 104 L 80 72 L 98 138 L 118 78 L 132 104 L 166 104"
          stroke="white"
          strokeOpacity="0.22"
          strokeWidth="6"
          strokeLinecap="round"
          strokeLinejoin="round"
        />

        {/* Animated ECG Pulse Stroke */}
        <motion.path
          d="M 34 104 L 66 104 L 80 72 L 98 138 L 118 78 L 132 104 L 166 104"
          stroke="#FFFFFF"
          strokeWidth="7"
          strokeLinecap="round"
          strokeLinejoin="round"
          filter="url(#npGlow)"
          initial={{ pathLength: 0, pathOffset: 0 }}
          animate={{
            pathLength: [0.15, 0.45, 0.15],
            pathOffset: [0, 1, 2]
          }}
          transition={{
            repeat: Infinity,
            duration: 2.2,
            ease: "linear"
          }}
        />

        {/* Glowing Pulse Nodes */}
        <motion.circle
          cx="80"
          cy="72"
          r="5"
          fill="#93C5FD"
          animate={{ scale: [1, 1.4, 1], opacity: [0.7, 1, 0.7] }}
          transition={{ repeat: Infinity, duration: 2.2, delay: 0.3 }}
        />
        <motion.circle
          cx="98"
          cy="138"
          r="6"
          fill="#34D399"
          animate={{ scale: [1, 1.5, 1], opacity: [0.7, 1, 0.7] }}
          transition={{ repeat: Infinity, duration: 2.2, delay: 0.6 }}
        />
        <motion.circle
          cx="118"
          cy="78"
          r="5"
          fill="#F472B6"
          animate={{ scale: [1, 1.4, 1], opacity: [0.7, 1, 0.7] }}
          transition={{ repeat: Infinity, duration: 2.2, delay: 0.9 }}
        />

        {/* Democracy Beacon */}
        <circle cx="100" cy="54" r="6.5" fill="#FFFFFF" />
        <motion.circle
          cx="100"
          cy="54"
          r="13"
          stroke="#60A5FA"
          strokeWidth="2"
          strokeOpacity="0.6"
          fill="none"
          animate={{ scale: [1, 1.6, 1], opacity: [0.3, 0.9, 0.3] }}
          transition={{ repeat: Infinity, duration: 2.2 }}
        />

        {/* Tricolor Green Bottom Arc */}
        <path d="M 58 166 Q 100 178 142 166" stroke="#138808" strokeWidth="4.5" strokeLinecap="round" fill="none" opacity="0.95" />
      </motion.svg>
    </div>
  );
};
