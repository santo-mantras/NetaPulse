import React, { useState } from 'react';

interface TickerItem {
    id: number;
    icon: string;
    category: string;
    text: string;
}

const TICKER_ITEMS: TickerItem[] = [
    {
        id: 1,
        icon: '🗳️',
        category: 'UPCOMING STATE ELECTIONS',
        text: 'West Bengal, Tamil Nadu, Kerala, Assam & Puducherry (Apr–May 2026) • Uttar Pradesh, Punjab, Goa & Gujarat (2027)'
    },
    {
        id: 2,
        icon: '🏛️',
        category: 'PARLIAMENT WATCH',
        text: '18th Lok Sabha completed 115+ hours of legislative business; upcoming session to table key governance and financial reforms'
    },
    {
        id: 3,
        icon: '💸',
        category: 'TAXPAYER COST PER SESSION',
        text: '₹2.5 Lakh spent every minute of Parliamentary sittings (~₹9.1 Crore per active sitting day funded by Indian taxpayers)'
    },
    {
        id: 4,
        icon: '🇮🇳',
        category: 'CURRENT PM & PRESIDENT',
        text: 'Prime Minister: Narendra Modi • President of India: Droupadi Murmu (15th President of the Republic)'
    },
    {
        id: 5,
        icon: '⚖️',
        category: 'ECI & CJI CHIEF HEADS',
        text: 'Chief Justice of India: Justice Sanjiv Khanna (51st CJI) • Chief Election Commissioner: Rajiv Kumar'
    }
];

export const CivicPulseTicker: React.FC = () => {
    const [isManualPaused, setIsManualPaused] = useState(false);
    const [isHovered, setIsHovered] = useState(false);

    // If hovered or manually paused, pause the ticker
    const isPaused = isManualPaused || isHovered;

    const handleMouseEnter = () => {
        setIsHovered(true);
    };

    const handleMouseLeave = () => {
        setIsHovered(false);
    };

    const handleClick = () => {
        // If it's currently paused (by hover or by click), clicking starts it moving again!
        // If it's currently moving, clicking stops it!
        if (isPaused) {
            setIsManualPaused(false);
            setIsHovered(false);
        } else {
            setIsManualPaused(true);
        }
    };

    const renderTickerTrack = () => (
        <div className="flex items-center shrink-0">
            {TICKER_ITEMS.map((item) => (
                <div key={item.id} className="inline-flex items-center gap-2 mr-12 shrink-0">
                    <span className="text-sm">{item.icon}</span>
                    <span className="text-amber-300 dark:text-amber-300 font-extrabold uppercase tracking-wider text-[11px] shrink-0">
                        {item.category}:
                    </span>
                    <span className="text-slate-100 font-medium text-xs whitespace-nowrap">
                        {item.text}
                    </span>
                    <span className="ml-12 text-indigo-300/40 select-none text-xs font-bold">✦</span>
                </div>
            ))}
        </div>
    );

    return (
        <div 
            onClick={handleClick}
            onMouseEnter={handleMouseEnter}
            onMouseLeave={handleMouseLeave}
            className="bg-indigo-700 dark:bg-indigo-950 text-white text-xs font-semibold py-2 overflow-hidden select-none border-b border-indigo-600/50 dark:border-indigo-800/60 relative z-40 cursor-pointer group"
            title={isPaused ? "Paused — Click anywhere to resume moving text" : "Moving text — Hover or click to pause"}
        >
            <style>{`
                @keyframes marqueeContinuous {
                    0% { transform: translateX(0%); }
                    100% { transform: translateX(-50%); }
                }
                .marquee-track {
                    display: flex;
                    width: max-content;
                    animation: marqueeContinuous 55s linear infinite;
                }
            `}</style>

            <div 
                className="marquee-track"
                style={{
                    animationPlayState: isPaused ? 'paused' : 'running'
                }}
            >
                {renderTickerTrack()}
                {renderTickerTrack()}
            </div>
        </div>
    );
};
