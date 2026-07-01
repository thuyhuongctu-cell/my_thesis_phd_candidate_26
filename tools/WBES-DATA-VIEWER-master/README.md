# WBES Schedule Data Viewer

A modern, client-side web application for visualizing and analyzing Web Based Energy Scheduling (WBES) data. This tool provides comprehensive data exploration, filtering, and analysis capabilities for energy trading operations.

![WBES Screenshot](https://via.placeholder.com/800x400?text=WBES+Schedule+Data+Viewer)

## 🚀 Live Demo

[**View Live Application**](https://your-username.github.io/wbes_view/)

## ✨ Features

### 🎨 **Modern Interface**
- **Dark/Light Mode Toggle** - Switch themes for comfortable viewing
- **Responsive Design** - Works perfectly on desktop, tablet, and mobile
- **Professional UI** - Clean, gradient-based design optimized for energy professionals

### 📊 **Data Visualization**
- **Interactive Charts** - Chart.js powered time-series visualization with 96 time blocks
- **Multi-dataset Overlays** - View Injection/Drawal boundaries simultaneously  
- **Smart Tooltips** - Shows both MW (instantaneous power) and MWh (energy per block)
- **Theme-aware Charts** - Chart colors automatically adapt to selected theme

### 🔍 **Advanced Data Analysis**
- **Group-wise Explorer** - Navigate through different energy groups and entities
- **9+ Filter System** - Filter by schedule type, seller, buyer, trader, power range, etc.
- **Real-time Results** - Live filtering with instant result count updates
- **4-Tab Detail Analysis** - Basic Info, Schedule Data, Loss Analysis, Boundary Data

### 📈 **Energy Calculations**
- **MW ↔ MWh Conversion** - Automatic conversion between power and energy units
- **15-minute Block Processing** - Handles standard power system scheduling intervals
- **Loss Analysis** - POC losses, boundary losses, efficiency calculations
- **Power Range Filtering** - Filter by average MW ranges (0-10, 10-50, 50-100, 100+)

### 💾 **Data Management**
- **File Picker Interface** - Load any WBES-compliant JSON file
- **Data Validation** - Automatic structure validation before loading
- **CSV Export** - Export filtered data with all calculations preserved
- **No Server Required** - Pure client-side operation for security and privacy

## 🛠️ Technology Stack

- **Frontend**: Pure HTML5, CSS3, JavaScript (ES6+)
- **Charts**: Chart.js for data visualization
- **Styling**: CSS Custom Properties for theming
- **Architecture**: Client-side only, no build tools required
- **Browser Support**: Chrome 90+, Firefox 90+, Safari 14+, Edge 90+

## 📁 Repository Structure

```
wbes_view/
├── index.html              # Main application
├── script.js               # Core application logic
├── styles.css              # Complete styling with themes
├── README.md               # This file
├── requirements.md         # Technical requirements
├── CLAUDE.md               # Development documentation
└── LICENSE                 # MIT License
```

## 🚀 Quick Start

### Option 1: GitHub Pages (Recommended)
1. Visit the [live application](https://your-username.github.io/wbes_view/)
2. Click "📁 Load JSON File" to upload your WBES data
3. Start exploring your energy scheduling data!

### Option 2: Local Development
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/wbes_view.git
   cd wbes_view
   ```

2. **Open in browser**
   ```bash
   # Simply open index.html in your preferred browser
   open index.html          # macOS
   start index.html         # Windows
   xdg-open index.html      # Linux
   ```

3. **Load your data**
   - Click the "📁 Load JSON File" button
   - Select your WBES JSON data file
   - The application will validate and load your data automatically

## 📊 Data Format Requirements

Your JSON file must follow the WBES data structure:

```json
{
  "ResponseBody": {
    "Date": "06-08-2025",
    "FullSchdRevisionNo": 115,
    "SchedulePublishedTime": "2025-08-06T16:48:00",
    "GroupWiseDataList": [
      {
        "Acronym": "GROUP_NAME",
        "FullschdList": [
          {
            "EnergyScheduleTypeName": "OA_TGNA",
            "SellerAcronym": "SELLER",
            "BuyerAcronym": "BUYER",
            "FullScheduleData": {
              "OAFullScheduleJsonData": {
                "SchdAmount": [/* 96 MW values for 15-min blocks */]
              }
            }
          }
        ]
      }
    ]
  }
}
```

### Supported Schedule Types
- **OA_TGNA** - Open Access Third Party Network Access
- **ISGS** - Inter-State Generation Scheduling (Thermal, Hydro, Gas, Nuclear)
- **Loss Data** - POC losses, boundary losses, state losses
- **Boundary Data** - Injection/Drawal flow information

## 🎯 Key Features Explained

### Energy Unit Conversion
- **Input**: MW values for 15-minute time blocks (96 blocks per day)
- **Automatic Conversion**: MW × 0.25 hours = MWh per block
- **Display**: Shows both instantaneous power (MW) and energy totals (MWh)

### Advanced Filtering System
- **Schedule Type**: OA_TGNA, ISGS
- **Sub Type**: Various energy trading sub-categories
- **Entities**: Filter by Seller, Buyer, Trader acronyms
- **Generator Type**: Thermal, Hydro, Gas, Nuclear
- **Power Range**: 0-10MW, 10-50MW, 50-100MW, 100+MW
- **Approval Status**: With/Without approval numbers

### Multi-Tab Analysis
1. **Basic Info**: Schedule metadata and entity information
2. **Schedule Data**: Energy values with MW/MWh calculations
3. **Loss Analysis**: POC losses, efficiency metrics
4. **Boundary Data**: Regional interconnection flows

## 🌙 Theme System

- **Light Mode**: Professional blue gradients with high contrast
- **Dark Mode**: Navy/gray theme optimized for extended analysis sessions
- **Persistent Choice**: Theme preference saved in localStorage
- **Comprehensive**: All elements including charts and tables adapt automatically

## 📱 Browser Compatibility

| Browser | Version | Status |
|---------|---------|--------|
| Chrome  | 90+     | ✅ Fully Supported |
| Firefox | 90+     | ✅ Fully Supported |
| Safari  | 14+     | ✅ Fully Supported |
| Edge    | 90+     | ✅ Fully Supported |

## 🔒 Security & Privacy

- **Client-side Only**: No data sent to external servers
- **Local Processing**: All analysis performed in your browser
- **No Data Storage**: Files processed temporarily, nothing persisted
- **CORS Compliant**: Works with local files and secure origins

## 📈 Performance

- **Fast Loading**: Loads within 3 seconds on standard connections
- **Responsive Filtering**: Filter results appear within 1 second
- **Large Dataset Support**: Handles files up to 10MB efficiently
- **Smooth Animations**: 60fps transitions and theme switching

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow existing code style and naming conventions
- Test with multiple WBES data formats
- Ensure theme compatibility for new features
- Update documentation for significant changes

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/wbes_view/issues)
- **Documentation**: [CLAUDE.md](CLAUDE.md) for developers
- **Requirements**: [requirements.md](requirements.md) for technical specs

## 🏗️ Built With

- [Chart.js](https://www.chartjs.org/) - Beautiful charts for JavaScript
- [CSS Custom Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/--*) - Theme system
- [File API](https://developer.mozilla.org/en-US/docs/Web/API/File) - Client-side file handling

## 📊 Project Stats

![GitHub repo size](https://img.shields.io/github/repo-size/your-username/wbes_view)
![GitHub language count](https://img.shields.io/github/languages/count/your-username/wbes_view)
![GitHub top language](https://img.shields.io/github/languages/top/your-username/wbes_view)
![GitHub last commit](https://img.shields.io/github/last-commit/your-username/wbes_view)

---

<div align="center">
  <p><strong>Empowering Energy Professionals with Modern Data Visualization</strong></p>
  <p>Made with ❤️ for the Energy Scheduling Industry</p>
</div>