import os

def create_emoji_svg(emoji, color, filename):
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
    <circle cx="50" cy="50" r="50" fill="{color}"/>
    <text x="50" y="55" font-size="60" dominant-baseline="middle" text-anchor="middle">{emoji}</text>
</svg>'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Created {filename}")

def main():
    parties_dir = "public/assets/parties"
    os.makedirs(parties_dir, exist_ok=True)
    
    symbols = {
        "BJP.svg": ("🪷", "#F97D09"),       # Lotus, Saffron
        "INC.svg": ("✋", "#00BFFF"),       # Hand, Blue
        "AAP.svg": ("🧹", "#005B9F"),       # Broom, Blue
        "Shiv Sena.svg": ("🏹", "#FF6600"), # Bow & Arrow, Saffron
        "NCP.svg": ("🕰️", "#003366"),      # Clock, Dark Blue
        "SAD.svg": ("⚖️", "#F58220"),       # Scales, Orange
        "MNS.svg": ("🚩", "#FF9933"),       # Flag, Saffron
        "Independent.svg": ("👤", "#808080")# Person, Gray
    }
    
    for filename, (emoji, color) in symbols.items():
        filepath = os.path.join(parties_dir, filename)
        create_emoji_svg(emoji, color, filepath)

if __name__ == "__main__":
    main()
