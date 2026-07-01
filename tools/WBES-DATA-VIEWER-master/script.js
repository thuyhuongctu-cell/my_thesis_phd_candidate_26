let scheduleData = null;
let currentChart = null;

// Theme management
function setupTheme() {
    // Check for saved theme preference or default to light mode
    const savedTheme = localStorage.getItem('wbes-theme') || 'light';
    applyTheme(savedTheme);
}

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    applyTheme(newTheme);
    localStorage.setItem('wbes-theme', newTheme);
}

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    
    // Update theme toggle icon
    const themeIcon = document.getElementById('theme-icon');
    if (themeIcon) {
        themeIcon.textContent = theme === 'light' ? '🌙' : '☀️';
    }
    
    // Update Chart.js colors if chart exists
    if (currentChart) {
        updateChartColors(theme);
    }
    
    // Force update all potentially stubborn elements
    const isDark = theme === 'dark';
    
    // Update chart containers
    const chartContainers = document.querySelectorAll('.chart-container, #chart-container');
    chartContainers.forEach(container => {
        container.style.backgroundColor = isDark ? '#16213e' : 'white';
    });
    
    // Update table containers
    const tableContainers = document.querySelectorAll('.data-table-container');
    tableContainers.forEach(container => {
        container.style.backgroundColor = isDark ? '#16213e' : 'white';
    });
    
    // Update all tables
    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        table.style.backgroundColor = isDark ? '#16213e' : 'white';
        table.style.color = isDark ? '#eee' : '#333';
    });
}

function updateChartColors(theme) {
    if (!currentChart) return;
    
    const isDark = theme === 'dark';
    const textColor = isDark ? '#eee' : '#333';
    const gridColor = isDark ? '#4a5568' : '#e0e6ed';
    
    // Update scales
    if (currentChart.options.scales.x) {
        currentChart.options.scales.x.ticks.color = textColor;
        currentChart.options.scales.x.grid.color = gridColor;
        if (currentChart.options.scales.x.title) {
            currentChart.options.scales.x.title.color = textColor;
        }
    }
    
    if (currentChart.options.scales.y) {
        currentChart.options.scales.y.ticks.color = textColor;
        currentChart.options.scales.y.grid.color = gridColor;
        if (currentChart.options.scales.y.title) {
            currentChart.options.scales.y.title.color = textColor;
        }
    }
    
    // Update plugins
    if (currentChart.options.plugins) {
        if (currentChart.options.plugins.legend && currentChart.options.plugins.legend.labels) {
            currentChart.options.plugins.legend.labels.color = textColor;
        }
        if (currentChart.options.plugins.title) {
            currentChart.options.plugins.title.color = textColor;
        }
    }
    
    // Update chart background
    const chartCanvas = currentChart.canvas;
    if (chartCanvas && chartCanvas.parentElement) {
        chartCanvas.parentElement.style.backgroundColor = isDark ? '#16213e' : 'white';
    }
    
    // Force chart update with animation disabled for immediate effect
    currentChart.update('none');
}

// Load JSON data when page loads
document.addEventListener('DOMContentLoaded', function() {
    setupTheme();
    setupFileLoader();
    loadScheduleData();
});

function setupFileLoader() {
    const fileInput = document.getElementById('json-file-input');
    
    fileInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file && file.type === 'application/json') {
            loadFileData(file);
        } else if (file) {
            updateFileStatus('Please select a valid JSON file', 'error');
        }
    });
}

function loadFileData(file) {
    updateFileStatus('Loading file...', 'loading');
    
    const reader = new FileReader();
    reader.onload = function(e) {
        try {
            const jsonData = JSON.parse(e.target.result);
            if (jsonData && jsonData.ResponseBody) {
                scheduleData = jsonData;
                updateFileStatus(`Loaded: ${file.name}`, 'success');
                initializeApplication();
            } else {
                updateFileStatus('Invalid JSON structure - missing ResponseBody', 'error');
            }
        } catch (error) {
            console.error('Error parsing JSON:', error);
            updateFileStatus('Error parsing JSON file', 'error');
        }
    };
    
    reader.onerror = function() {
        updateFileStatus('Error reading file', 'error');
    };
    
    reader.readAsText(file);
}

function updateFileStatus(message, type) {
    const statusElement = document.getElementById('file-status');
    statusElement.textContent = message;
    
    // Remove existing status classes
    statusElement.classList.remove('status-success', 'status-error', 'status-loading');
    
    // Add appropriate status class
    if (type) {
        statusElement.classList.add(`status-${type}`);
    }
}

async function loadScheduleData() {
    try {
        console.log('Application ready - waiting for user to load JSON file');
        
        if (!scheduleData) {
            console.log('No data loaded. User must select a JSON file.');
            clearAllSections();
        }
    } catch (error) {
        console.error('Error initializing application:', error);
        document.getElementById('date').textContent = 'Error initializing - check console';
    }
}

function clearAllSections() {
    // Clear overview section
    document.getElementById('date').textContent = 'Please load a JSON file to begin';
    document.getElementById('revision').textContent = 'No data';
    document.getElementById('published-time').textContent = 'No data';
    document.getElementById('schedule-type').textContent = 'Please load data';
    document.getElementById('total-records').textContent = '0';
    document.getElementById('schedule-remarks').textContent = 'Load a JSON file to view data';
    
    // Clear group-wise data section
    const groupSelect = document.getElementById('group-select');
    if (groupSelect) {
        groupSelect.innerHTML = '<option value="">No data loaded</option>';
    }
    
    const groupOverviewList = document.getElementById('group-overview-list');
    if (groupOverviewList) {
        groupOverviewList.innerHTML = '<p class="no-data-message">Please load a JSON file to explore group data</p>';
    }
    
    const groupContent = document.getElementById('group-content');
    if (groupContent) {
        groupContent.innerHTML = '<p class="no-data-message">No data available</p>';
    }
    
    const groupStats = document.getElementById('group-stats');
    if (groupStats) {
        groupStats.innerHTML = '';
    }
    
    // Hide filter panel
    const filterPanel = document.getElementById('filter-panel');
    if (filterPanel) {
        filterPanel.style.display = 'none';
    }
    
    // Clear schedule types section
    const scheduleTypesList = document.getElementById('schedule-types-list');
    if (scheduleTypesList) {
        scheduleTypesList.innerHTML = '<p class="no-data-message">Load a JSON file to view schedule types</p>';
    }
    
    // Clear chart and detail sections
    const chartContainer = document.getElementById('chart-container');
    if (chartContainer) {
        chartContainer.innerHTML = '<p class="no-data-message">Chart will appear when data is loaded</p>';
    }
    
    const detailTabs = document.getElementById('detail-tabs');
    if (detailTabs) {
        detailTabs.style.display = 'none';
    }
}

function initializeApplication() {
    try {
        if (scheduleData && scheduleData.ResponseBody) {
            console.log('Valid data structure found');
            displayOverviewInfo();
            setupGroupWiseData();
            displayScheduleTypes();
            setupInitialChart();
        } else {
            console.error('Invalid data structure');
            document.getElementById('date').textContent = 'Invalid data structure';
        }
    } catch (error) {
        console.error('Error initializing application:', error);
        updateFileStatus('Error initializing application', 'error');
    }
}

function displayOverviewInfo() {
    const responseBody = scheduleData.ResponseBody;
    
    document.getElementById('date').textContent = `Date: ${responseBody.Date}`;
    document.getElementById('revision').textContent = `Revision: ${responseBody.FullSchdRevisionNo}`;
    document.getElementById('published-time').textContent = `Published: ${responseBody.SchedulePublishedTime}`;
    document.getElementById('schedule-remarks').textContent = responseBody.ScheduleRemarks || 'No remarks';
    document.getElementById('schedule-type').textContent = 'WBES Energy Schedule';
    
    // Count total records
    let totalRecords = 0;
    if (responseBody.GroupWiseDataList) {
        responseBody.GroupWiseDataList.forEach(group => {
            if (group.FullschdList) {
                totalRecords += group.FullschdList.length;
            }
        });
    }
    document.getElementById('total-records').textContent = totalRecords;
}

function setupGroupWiseData() {
    const responseBody = scheduleData.ResponseBody;
    const groupSelect = document.getElementById('group-select');
    const groupOverviewList = document.getElementById('group-overview-list');
    
    // Clear existing options
    groupSelect.innerHTML = '<option value="">Select a group...</option>';
    groupOverviewList.innerHTML = '';
    
    if (responseBody.GroupWiseDataList) {
        responseBody.GroupWiseDataList.forEach((group, groupIndex) => {
            // Add to group selector
            const option = document.createElement('option');
            option.value = groupIndex;
            option.textContent = `${group.Acronym} (${group.FullschdList ? group.FullschdList.length : 0} schedules)`;
            groupSelect.appendChild(option);
            
            // Create group overview card
            const groupCard = createGroupOverviewCard(group, groupIndex);
            groupOverviewList.appendChild(groupCard);
        });
    }
}

function createGroupOverviewCard(group, groupIndex) {
    const card = document.createElement('div');
    card.className = 'group-overview-card';
    card.dataset.groupIndex = groupIndex;
    
    const scheduleCount = group.FullschdList ? group.FullschdList.length : 0;
    const oaCount = group.FullschdList ? group.FullschdList.filter(s => s.EnergyScheduleTypeName === 'OA_TGNA').length : 0;
    const isgsCount = group.FullschdList ? group.FullschdList.filter(s => s.EnergyScheduleTypeName === 'ISGS').length : 0;
    
    card.innerHTML = `
        <div class="group-header">
            <h3>${group.Acronym}</h3>
            <span class="schedule-count">${scheduleCount} schedules</span>
        </div>
        <div class="group-breakdown">
            <div class="breakdown-item">
                <span class="breakdown-label">OA Schedules:</span>
                <span class="breakdown-value">${oaCount}</span>
            </div>
            <div class="breakdown-item">
                <span class="breakdown-label">ISGS Schedules:</span>
                <span class="breakdown-value">${isgsCount}</span>
            </div>
        </div>
        <div class="group-actions">
            <button onclick="showGroupData(${groupIndex})" class="btn-explore">Explore Group</button>
        </div>
    `;
    
    return card;
}

function showGroupData(groupIndex = null) {
    if (groupIndex === null) {
        const selectElement = document.getElementById('group-select');
        groupIndex = selectElement.value;
    }
    
    if (!groupIndex || groupIndex === '') {
        document.getElementById('group-content').innerHTML = '<p class="placeholder-text">Select a group to view detailed information</p>';
        document.getElementById('group-stats').innerHTML = '';
        document.getElementById('filter-panel').style.display = 'none';
        return;
    }
    
    const group = scheduleData.ResponseBody.GroupWiseDataList[groupIndex];
    window.currentGroup = group;
    window.currentGroupIndex = groupIndex;
    
    // Show filter panel
    document.getElementById('filter-panel').style.display = 'block';
    
    // Populate filter options
    populateFilterOptions(group);
    
    // Update group selector if called from button
    document.getElementById('group-select').value = groupIndex;
    
    // Display schedules (initially unfiltered)
    displayGroupSchedules(group, groupIndex);
}

function populateFilterOptions(group) {
    if (!group.FullschdList) return;
    
    const schedules = group.FullschdList;
    
    // Get unique values for each filter
    const scheduleTypes = [...new Set(schedules.map(s => s.EnergyScheduleTypeName))];
    const subTypes = [...new Set(schedules.map(s => s.EnergyScheduleSubTypeName))];
    const links = [...new Set(schedules.map(s => s.LinkName))];
    const sellers = [...new Set(schedules.map(s => s.SellerAcronym))];
    const buyers = [...new Set(schedules.map(s => s.BuyerAcronym))];
    const traders = [...new Set(schedules.map(s => s.TraderAcronym).filter(t => t && t.trim()))];
    
    // Populate dropdowns
    populateSelect('schedule-type-filter', scheduleTypes, 'All Types');
    populateSelect('schedule-subtype-filter', subTypes, 'All Sub Types');
    populateSelect('link-filter', links, 'All Links');
    populateSelect('seller-filter', sellers, 'All Sellers');
    populateSelect('buyer-filter', buyers, 'All Buyers');
    populateSelect('trader-filter', traders, 'All Traders');
}

function populateSelect(selectId, options, defaultText) {
    const select = document.getElementById(selectId);
    select.innerHTML = `<option value="">${defaultText}</option>`;
    
    options.sort().forEach(option => {
        if (option && option.trim()) {
            const optionEl = document.createElement('option');
            optionEl.value = option;
            optionEl.textContent = option;
            select.appendChild(optionEl);
        }
    });
}

function displayGroupSchedules(group, groupIndex, filteredSchedules = null) {
    const groupStats = document.getElementById('group-stats');
    const groupContent = document.getElementById('group-content');
    
    const schedulesToShow = filteredSchedules || group.FullschdList || [];
    const totalSchedules = group.FullschdList ? group.FullschdList.length : 0;
    
    // Update group stats
    groupStats.innerHTML = `
        <div class="stat-item">
            <span class="stat-label">Group:</span>
            <span class="stat-value">${group.Acronym}</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">Showing:</span>
            <span class="stat-value">${schedulesToShow.length} of ${totalSchedules}</span>
        </div>
    `;
    
    // Update filter count
    const filterCount = document.getElementById('filter-count');
    if (filteredSchedules) {
        filterCount.textContent = `${schedulesToShow.length} schedules match filters`;
        filterCount.style.display = 'inline';
    } else {
        filterCount.style.display = 'none';
    }
    
    // Display group schedules
    let contentHTML = `
        <div class="group-schedules">
            <h3>Schedules for ${group.Acronym}</h3>
    `;
    
    if (schedulesToShow.length === 0) {
        contentHTML += '<p class="placeholder-text">No schedules match the current filters</p>';
    } else {
        contentHTML += '<div class="schedule-grid">';
        
        schedulesToShow.forEach((schedule, displayIndex) => {
            // Find the original index in the group's FullschdList
            const originalIndex = group.FullschdList.indexOf(schedule);
            const totalMWh = calculateSchedulePower(schedule, 'total_mwh');
            const avgMW = calculateSchedulePower(schedule, 'average');
            const generatorType = getGeneratorType(schedule);
            
            contentHTML += `
                <div class="schedule-drill-card" onclick="displayScheduleDetails(${groupIndex}, ${originalIndex})">
                    <div class="drill-card-header">
                        <h4>${schedule.EnergyScheduleTypeName}</h4>
                        <span class="schedule-type-badge">${schedule.EnergyScheduleSubTypeName}</span>
                    </div>
                    <div class="drill-card-body">
                        <p><strong>Seller:</strong> ${schedule.SellerAcronym}</p>
                        <p><strong>Buyer:</strong> ${schedule.BuyerAcronym}</p>
                        <p><strong>Link:</strong> ${schedule.LinkName}</p>
                        ${schedule.ApprovalNo ? `<p><strong>Approval:</strong> ${schedule.ApprovalNo}</p>` : ''}
                        ${schedule.TraderAcronym ? `<p><strong>Trader:</strong> ${schedule.TraderAcronym}</p>` : ''}
                        ${generatorType ? `<p><strong>Generator:</strong> ${generatorType}</p>` : ''}
                        <p><strong>Total Energy:</strong> ${totalMWh} MWh</p>
                        <p><strong>Avg Power:</strong> ${avgMW} MW</p>
                    </div>
                    <div class="drill-card-footer">
                        <button class="btn-drill-down">View Details</button>
                    </div>
                </div>
            `;
        });
        
        contentHTML += '</div>';
    }
    
    contentHTML += '</div>';
    groupContent.innerHTML = contentHTML;
}

function applyFilters() {
    if (!window.currentGroup) return;
    
    const schedules = window.currentGroup.FullschdList || [];
    const filters = getActiveFilters();
    
    const filteredSchedules = schedules.filter(schedule => {
        // Schedule Type filter
        if (filters.scheduleType && schedule.EnergyScheduleTypeName !== filters.scheduleType) {
            return false;
        }
        
        // Schedule Sub Type filter
        if (filters.scheduleSubtype && schedule.EnergyScheduleSubTypeName !== filters.scheduleSubtype) {
            return false;
        }
        
        // Link filter
        if (filters.link && schedule.LinkName !== filters.link) {
            return false;
        }
        
        // Seller filter
        if (filters.seller && schedule.SellerAcronym !== filters.seller) {
            return false;
        }
        
        // Buyer filter
        if (filters.buyer && schedule.BuyerAcronym !== filters.buyer) {
            return false;
        }
        
        // Trader filter
        if (filters.trader && schedule.TraderAcronym !== filters.trader) {
            return false;
        }
        
        // Generator type filter
        if (filters.generatorType) {
            const scheduleGeneratorType = getGeneratorType(schedule);
            if (scheduleGeneratorType !== filters.generatorType) {
                return false;
            }
        }
        
        // Has approval filter
        if (filters.hasApproval !== '') {
            const hasApproval = schedule.ApprovalNo && schedule.ApprovalNo.trim() !== '';
            if ((filters.hasApproval === 'yes' && !hasApproval) || 
                (filters.hasApproval === 'no' && hasApproval)) {
                return false;
            }
        }
        
        // Power range filter (using average MW for filtering)
        if (filters.powerRange) {
            const avgPower = calculateSchedulePower(schedule, 'average');
            if (!isInPowerRange(avgPower, filters.powerRange)) {
                return false;
            }
        }
        
        return true;
    });
    
    displayGroupSchedules(window.currentGroup, window.currentGroupIndex, filteredSchedules);
}

function getActiveFilters() {
    return {
        scheduleType: document.getElementById('schedule-type-filter').value,
        scheduleSubtype: document.getElementById('schedule-subtype-filter').value,
        link: document.getElementById('link-filter').value,
        seller: document.getElementById('seller-filter').value,
        buyer: document.getElementById('buyer-filter').value,
        trader: document.getElementById('trader-filter').value,
        generatorType: document.getElementById('generator-type-filter').value,
        hasApproval: document.getElementById('has-approval-filter').value,
        powerRange: document.getElementById('power-range-filter').value
    };
}

function calculateSchedulePower(schedule, returnType = 'total') {
    const scheduleData = schedule.FullScheduleData;
    let totalMW = 0;
    let dataPoints = 0;
    
    if (scheduleData.OAFullScheduleJsonData && scheduleData.OAFullScheduleJsonData.SchdAmount) {
        const amounts = scheduleData.OAFullScheduleJsonData.SchdAmount;
        totalMW = amounts.reduce((a, b) => a + b, 0);
        dataPoints = amounts.length;
    } else if (scheduleData.ISGSFullScheduleJsonData) {
        const isgsData = scheduleData.ISGSFullScheduleJsonData;
        if (isgsData.ISGSThermalFullScheduleJsonData && isgsData.ISGSThermalFullScheduleJsonData.OnbarSchdAmount) {
            const amounts = isgsData.ISGSThermalFullScheduleJsonData.OnbarSchdAmount;
            totalMW = amounts.reduce((a, b) => a + b, 0);
            dataPoints = amounts.length;
        } else if (isgsData.ISGSHydroFullScheduleJsonData && isgsData.ISGSHydroFullScheduleJsonData.SchdAmount) {
            const amounts = isgsData.ISGSHydroFullScheduleJsonData.SchdAmount;
            totalMW = amounts.reduce((a, b) => a + b, 0);
            dataPoints = amounts.length;
        }
    }
    
    // Convert MW blocks to MWh (each block is 15 minutes = 0.25 hours)
    const totalMWh = totalMW * 0.25;
    const avgMW = dataPoints > 0 ? totalMW / dataPoints : 0;
    
    if (returnType === 'average') {
        return avgMW.toFixed(2);
    } else if (returnType === 'total_mwh') {
        return totalMWh.toFixed(2);
    } else {
        return totalMWh.toFixed(2); // Default to MWh
    }
}

function getGeneratorType(schedule) {
    const scheduleData = schedule.FullScheduleData;
    if (scheduleData.ISGSFullScheduleJsonData) {
        return scheduleData.ISGSFullScheduleJsonData.ISGSGeneratorTypeName;
    }
    return null;
}

function isInPowerRange(power, range) {
    const powerNum = parseFloat(power);
    switch (range) {
        case '0-10':
            return powerNum >= 0 && powerNum <= 10;
        case '10-50':
            return powerNum > 10 && powerNum <= 50;
        case '50-100':
            return powerNum > 50 && powerNum <= 100;
        case '100+':
            return powerNum > 100;
        default:
            return true;
    }
}

function resetFilters() {
    // Reset all filter dropdowns
    document.getElementById('schedule-type-filter').value = '';
    document.getElementById('schedule-subtype-filter').value = '';
    document.getElementById('link-filter').value = '';
    document.getElementById('seller-filter').value = '';
    document.getElementById('buyer-filter').value = '';
    document.getElementById('trader-filter').value = '';
    document.getElementById('generator-type-filter').value = '';
    document.getElementById('has-approval-filter').value = '';
    document.getElementById('power-range-filter').value = '';
    
    // Reapply filters (which will now show all schedules)
    applyFilters();
}

function exportFilteredData() {
    if (!window.currentGroup) {
        alert('Please select a group first');
        return;
    }
    
    const schedules = window.currentGroup.FullschdList || [];
    const filters = getActiveFilters();
    const hasActiveFilters = Object.values(filters).some(filter => filter !== '');
    
    const dataToExport = hasActiveFilters ? 
        schedules.filter(schedule => {
            // Apply the same filtering logic as in applyFilters()
            if (filters.scheduleType && schedule.EnergyScheduleTypeName !== filters.scheduleType) return false;
            if (filters.scheduleSubtype && schedule.EnergyScheduleSubTypeName !== filters.scheduleSubtype) return false;
            if (filters.link && schedule.LinkName !== filters.link) return false;
            if (filters.seller && schedule.SellerAcronym !== filters.seller) return false;
            if (filters.buyer && schedule.BuyerAcronym !== filters.buyer) return false;
            if (filters.trader && schedule.TraderAcronym !== filters.trader) return false;
            if (filters.generatorType && getGeneratorType(schedule) !== filters.generatorType) return false;
            if (filters.hasApproval !== '') {
                const hasApproval = schedule.ApprovalNo && schedule.ApprovalNo.trim() !== '';
                if ((filters.hasApproval === 'yes' && !hasApproval) || 
                    (filters.hasApproval === 'no' && hasApproval)) return false;
            }
            if (filters.powerRange && !isInPowerRange(calculateSchedulePower(schedule, 'average'), filters.powerRange)) return false;
            return true;
        }) : schedules;
    
    // Create CSV content
    const headers = ['Group', 'Schedule Type', 'Sub Type', 'Seller', 'Buyer', 'Link', 'Approval No', 'Trader', 'Generator Type', 'Total Energy (MWh)', 'Avg Power (MW)'];
    let csvContent = headers.join(',') + '\n';
    
    dataToExport.forEach(schedule => {
        const row = [
            window.currentGroup.Acronym,
            schedule.EnergyScheduleTypeName || '',
            schedule.EnergyScheduleSubTypeName || '',
            schedule.SellerAcronym || '',
            schedule.BuyerAcronym || '',
            schedule.LinkName || '',
            schedule.ApprovalNo || '',
            schedule.TraderAcronym || '',
            getGeneratorType(schedule) || '',
            calculateSchedulePower(schedule, 'total_mwh'),
            calculateSchedulePower(schedule, 'average')
        ].map(field => `"${field}"`).join(',');
        csvContent += row + '\n';
    });
    
    // Download the file
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${window.currentGroup.Acronym}_filtered_schedules.csv`;
    link.click();
    window.URL.revokeObjectURL(url);
}

function displayScheduleTypes() {
    const responseBody = scheduleData.ResponseBody;
    const oaScheduleList = document.getElementById('oa-schedule-list');
    const isgsScheduleList = document.getElementById('isgs-schedule-list');
    const allScheduleList = document.getElementById('all-schedule-list');
    
    oaScheduleList.innerHTML = '';
    isgsScheduleList.innerHTML = '';
    allScheduleList.innerHTML = '';
    
    if (responseBody.GroupWiseDataList) {
        responseBody.GroupWiseDataList.forEach((group, groupIndex) => {
            if (group.FullschdList) {
                group.FullschdList.forEach((schedule, scheduleIndex) => {
                    const scheduleCard = createScheduleCard(schedule, groupIndex, scheduleIndex, group.Acronym);
                    
                    // Add to appropriate lists
                    allScheduleList.appendChild(scheduleCard.cloneNode(true));
                    
                    if (schedule.EnergyScheduleTypeName === 'OA_TGNA') {
                        oaScheduleList.appendChild(scheduleCard.cloneNode(true));
                    } else if (schedule.EnergyScheduleTypeName === 'ISGS') {
                        isgsScheduleList.appendChild(scheduleCard.cloneNode(true));
                    }
                });
            }
        });
    }
    
    // Add click listeners to all schedule cards
    document.querySelectorAll('.schedule-card, .schedule-drill-card').forEach(card => {
        card.addEventListener('click', function() {
            const groupIndex = this.dataset.groupIndex;
            const scheduleIndex = this.dataset.scheduleIndex;
            if (groupIndex !== undefined && scheduleIndex !== undefined) {
                displayScheduleDetails(groupIndex, scheduleIndex);
            }
        });
    });
}

function createScheduleCard(schedule, groupIndex, scheduleIndex, groupAcronym = '') {
    const card = document.createElement('div');
    card.className = 'schedule-card';
    card.dataset.groupIndex = groupIndex;
    card.dataset.scheduleIndex = scheduleIndex;
    
    card.innerHTML = `
        <div class="schedule-header">
            <h4>${schedule.EnergyScheduleTypeName}</h4>
            <span class="link-name">${schedule.LinkName}</span>
        </div>
        <div class="schedule-info">
            ${groupAcronym ? `<p><strong>Group:</strong> ${groupAcronym}</p>` : ''}
            <p><strong>Seller:</strong> ${schedule.SellerAcronym}</p>
            <p><strong>Buyer:</strong> ${schedule.BuyerAcronym}</p>
            ${schedule.ApprovalNo ? `<p><strong>Approval:</strong> ${schedule.ApprovalNo}</p>` : ''}
            ${schedule.TraderAcronym ? `<p><strong>Trader:</strong> ${schedule.TraderAcronym}</p>` : ''}
        </div>
    `;
    
    return card;
}

function displayScheduleDetails(groupIndex, scheduleIndex) {
    const group = scheduleData.ResponseBody.GroupWiseDataList[groupIndex];
    const schedule = group.FullschdList[scheduleIndex];
    
    // Store current selection for other tabs
    window.currentSchedule = { group, schedule, groupIndex, scheduleIndex };
    
    // Update basic info tab
    updateBasicInfo(group, schedule);
    
    // Update other tabs
    updateScheduleDataTab(schedule);
    updateLossAnalysisTab(schedule);
    updateBoundaryDataTab(schedule);
    
    // Update chart and table with this schedule's data
    updateHourlyData(schedule);
}

function updateBasicInfo(group, schedule) {
    const detailsContainer = document.getElementById('schedule-details-content');
    
    let detailsHTML = `
        <div class="details-card">
            <h3>${schedule.EnergyScheduleTypeName} - ${schedule.SellerAcronym} to ${schedule.BuyerAcronym}</h3>
            <div class="details-grid">
                <div class="detail-item">
                    <label>Group:</label>
                    <span>${group.Acronym}</span>
                </div>
                <div class="detail-item">
                    <label>Energy Schedule Type:</label>
                    <span>${schedule.EnergyScheduleTypeName}</span>
                </div>
                <div class="detail-item">
                    <label>Sub Type:</label>
                    <span>${schedule.EnergyScheduleSubTypeName}</span>
                </div>
                <div class="detail-item">
                    <label>Link Name:</label>
                    <span>${schedule.LinkName}</span>
                </div>
                <div class="detail-item">
                    <label>Seller:</label>
                    <span>${schedule.SellerAcronym}</span>
                </div>
                <div class="detail-item">
                    <label>Seller State:</label>
                    <span>${schedule.SellerParentStateUtilAcronym || 'N/A'}</span>
                </div>
                <div class="detail-item">
                    <label>Buyer:</label>
                    <span>${schedule.BuyerAcronym}</span>
                </div>
                <div class="detail-item">
                    <label>Buyer State:</label>
                    <span>${schedule.BuyerParentStateUtilAcronym || 'N/A'}</span>
                </div>
                ${schedule.ApprovalNo ? `<div class="detail-item"><label>Approval No:</label><span>${schedule.ApprovalNo}</span></div>` : ''}
                ${schedule.TraderAcronym ? `<div class="detail-item"><label>Trader:</label><span>${schedule.TraderAcronym}</span></div>` : ''}
                <div class="detail-item">
                    <label>Unit Wise Seller:</label>
                    <span>${schedule.IsUnitWiseSellerFlag ? 'Yes' : 'No'}</span>
                </div>
                <div class="detail-item">
                    <label>Unit Wise Buyer:</label>
                    <span>${schedule.IsUnitWiseBuyerFlag ? 'Yes' : 'No'}</span>
                </div>
            </div>
        </div>
    `;
    
    detailsContainer.innerHTML = detailsHTML;
}

function updateScheduleDataTab(schedule) {
    const container = document.getElementById('schedule-data-content');
    const scheduleData = schedule.FullScheduleData;
    
    let content = '<div class="schedule-data-overview"><h3>Available Schedule Data Types</h3>';
    
    // Check what data is available
    const dataTypes = [];
    
    if (scheduleData.OAFullScheduleJsonData) {
        dataTypes.push({name: 'Open Access (OA)', data: scheduleData.OAFullScheduleJsonData, key: 'OA'});
    }
    
    if (scheduleData.ISGSFullScheduleJsonData) {
        const isgsData = scheduleData.ISGSFullScheduleJsonData;
        if (isgsData.ISGSThermalFullScheduleJsonData) {
            dataTypes.push({name: 'ISGS Thermal', data: isgsData.ISGSThermalFullScheduleJsonData, key: 'ISGS_THERMAL'});
        }
        if (isgsData.ISGSHydroFullScheduleJsonData) {
            dataTypes.push({name: 'ISGS Hydro', data: isgsData.ISGSHydroFullScheduleJsonData, key: 'ISGS_HYDRO'});
        }
        if (isgsData.ISGSGasFullScheduleJsonData) {
            dataTypes.push({name: 'ISGS Gas', data: isgsData.ISGSGasFullScheduleJsonData, key: 'ISGS_GAS'});
        }
        if (isgsData.ISGSNuclearFullScheduleJsonData) {
            dataTypes.push({name: 'ISGS Nuclear', data: isgsData.ISGSNuclearFullScheduleJsonData, key: 'ISGS_NUCLEAR'});
        }
    }
    
    if (dataTypes.length === 0) {
        content += '<p>No schedule data available for this item.</p>';
    } else {
        content += '<div class="data-type-cards">';
        dataTypes.forEach(type => {
            const amounts = type.data.SchdAmount || type.data.OnbarSchdAmount || [];
            const totalMW = amounts.length > 0 ? amounts.reduce((a, b) => a + b, 0) : 0;
            const totalMWh = totalMW * 0.25; // Convert to MWh
            const avgMW = amounts.length > 0 ? totalMW / amounts.length : 0;
            
            content += `
                <div class="data-type-card">
                    <h4>${type.name}</h4>
                    <p><strong>Total Energy:</strong> ${totalMWh.toFixed(2)} MWh</p>
                    <p><strong>Avg Power:</strong> ${avgMW.toFixed(2)} MW</p>
                    <p><strong>Data Points:</strong> ${amounts.length}</p>
                </div>
            `;
        });
        content += '</div>';
    }
    
    content += '</div>';
    container.innerHTML = content;
}

function updateLossAnalysisTab(schedule) {
    const container = document.getElementById('loss-analysis-content');
    let content = '<div class="loss-analysis"><h3>Loss Analysis</h3>';
    
    // Get the active schedule data
    let activeData = null;
    if (schedule.FullScheduleData.OAFullScheduleJsonData) {
        activeData = schedule.FullScheduleData.OAFullScheduleJsonData;
    } else if (schedule.FullScheduleData.ISGSFullScheduleJsonData) {
        const isgsData = schedule.FullScheduleData.ISGSFullScheduleJsonData;
        activeData = isgsData.ISGSThermalFullScheduleJsonData || isgsData.ISGSHydroFullScheduleJsonData;
    }
    
    if (activeData) {
        const pocInjLossMW = activeData.POCInjectionLoss ? activeData.POCInjectionLoss.reduce((a, b) => a + b, 0) : 0;
        const pocDrwLossMW = activeData.POCDrawalLoss ? activeData.POCDrawalLoss.reduce((a, b) => a + b, 0) : 0;
        const stateInjLossMW = activeData.StateInjectionLoss ? activeData.StateInjectionLoss.reduce((a, b) => a + b, 0) : 0;
        const stateDrwLossMW = activeData.StateDrawalLoss ? activeData.StateDrawalLoss.reduce((a, b) => a + b, 0) : 0;
        
        // Convert to MWh
        const pocInjLossMWh = pocInjLossMW * 0.25;
        const pocDrwLossMWh = pocDrwLossMW * 0.25;
        const stateInjLossMWh = stateInjLossMW * 0.25;
        const stateDrwLossMWh = stateDrwLossMW * 0.25;
        const totalLossMWh = pocInjLossMWh + pocDrwLossMWh + stateInjLossMWh + stateDrwLossMWh;
        
        content += `
            <div class="loss-summary">
                <div class="loss-item">
                    <h4>POC Injection Loss</h4>
                    <p class="loss-value">${pocInjLossMWh.toFixed(2)} MWh</p>
                    <p class="loss-avg">Avg: ${(pocInjLossMW / 96).toFixed(3)} MW</p>
                </div>
                <div class="loss-item">
                    <h4>POC Drawal Loss</h4>
                    <p class="loss-value">${pocDrwLossMWh.toFixed(2)} MWh</p>
                    <p class="loss-avg">Avg: ${(pocDrwLossMW / 96).toFixed(3)} MW</p>
                </div>
                <div class="loss-item">
                    <h4>State Injection Loss</h4>
                    <p class="loss-value">${stateInjLossMWh.toFixed(2)} MWh</p>
                    <p class="loss-avg">Avg: ${(stateInjLossMW / 96).toFixed(3)} MW</p>
                </div>
                <div class="loss-item">
                    <h4>State Drawal Loss</h4>
                    <p class="loss-value">${stateDrwLossMWh.toFixed(2)} MWh</p>
                    <p class="loss-avg">Avg: ${(stateDrwLossMW / 96).toFixed(3)} MW</p>
                </div>
            </div>
            <div class="loss-details">
                <p><strong>Total Energy Losses:</strong> ${totalLossMWh.toFixed(2)} MWh</p>
                <p><strong>Total Loss Percentage:</strong> ${((totalLossMWh / (activeData.SchdAmount ? activeData.SchdAmount.reduce((a, b) => a + b, 0) * 0.25 : 1)) * 100).toFixed(2)}%</p>
            </div>
        `;
    } else {
        content += '<p>No loss data available for this schedule.</p>';
    }
    
    content += '</div>';
    container.innerHTML = content;
}

function updateBoundaryDataTab(schedule) {
    const container = document.getElementById('boundary-data-content');
    let content = '<div class="boundary-analysis"><h3>Boundary Data Analysis</h3>';
    
    // Get the active schedule data
    let activeData = null;
    if (schedule.FullScheduleData.OAFullScheduleJsonData) {
        activeData = schedule.FullScheduleData.OAFullScheduleJsonData;
    } else if (schedule.FullScheduleData.ISGSFullScheduleJsonData) {
        const isgsData = schedule.FullScheduleData.ISGSFullScheduleJsonData;
        activeData = isgsData.ISGSThermalFullScheduleJsonData || isgsData.ISGSHydroFullScheduleJsonData;
    }
    
    if (activeData) {
        const totalRegBoundaryMW = activeData.TotalRegBoundarySchdAmount ? 
            activeData.TotalRegBoundarySchdAmount.reduce((a, b) => a + b, 0) : 0;
        const totalInjBoundaryMW = activeData.TotalInjBoundarySchdAmount ? 
            activeData.TotalInjBoundarySchdAmount.reduce((a, b) => a + b, 0) : 0;
        const totalDrwBoundaryMW = activeData.TotalDrwBoundarySchdAmount ? 
            activeData.TotalDrwBoundarySchdAmount.reduce((a, b) => a + b, 0) : 0;
        
        // Convert to MWh
        const totalRegBoundaryMWh = totalRegBoundaryMW * 0.25;
        const totalInjBoundaryMWh = totalInjBoundaryMW * 0.25;
        const totalDrwBoundaryMWh = totalDrwBoundaryMW * 0.25;
        const netBoundaryMWh = totalInjBoundaryMWh - totalDrwBoundaryMWh;
        
        content += `
            <div class="boundary-summary">
                <div class="boundary-item">
                    <h4>Total Regional Boundary</h4>
                    <p class="boundary-value">${totalRegBoundaryMWh.toFixed(2)} MWh</p>
                    <p class="boundary-avg">Avg: ${(totalRegBoundaryMW / 96).toFixed(2)} MW</p>
                </div>
                <div class="boundary-item">
                    <h4>Total Injection Boundary</h4>
                    <p class="boundary-value">${totalInjBoundaryMWh.toFixed(2)} MWh</p>
                    <p class="boundary-avg">Avg: ${(totalInjBoundaryMW / 96).toFixed(2)} MW</p>
                </div>
                <div class="boundary-item">
                    <h4>Total Drawal Boundary</h4>
                    <p class="boundary-value">${totalDrwBoundaryMWh.toFixed(2)} MWh</p>
                    <p class="boundary-avg">Avg: ${(totalDrwBoundaryMW / 96).toFixed(2)} MW</p>
                </div>
            </div>
            <div class="boundary-details">
                <p><strong>Net Boundary Energy Flow:</strong> ${netBoundaryMWh.toFixed(2)} MWh</p>
                <p><strong>Boundary Efficiency:</strong> ${totalInjBoundaryMWh > 0 ? ((totalDrwBoundaryMWh / totalInjBoundaryMWh) * 100).toFixed(2) : 0}%</p>
                <p><strong>Energy Loss in Transmission:</strong> ${(totalInjBoundaryMWh - totalDrwBoundaryMWh).toFixed(2)} MWh</p>
            </div>
        `;
    } else {
        content += '<p>No boundary data available for this schedule.</p>';
    }
    
    content += '</div>';
    container.innerHTML = content;
}

// Function to handle detail tab switching
function showDetailTab(tabName) {
    // Hide all detail tab contents
    document.querySelectorAll('.detail-tab-content').forEach(content => {
        content.classList.remove('active');
    });
    
    // Remove active class from all detail tabs
    document.querySelectorAll('.detail-tab-button').forEach(button => {
        button.classList.remove('active');
    });
    
    // Show selected detail tab content
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked detail tab
    event.target.classList.add('active');
}

function updateHourlyData(schedule) {
    let scheduleDataObj = null;
    
    // Determine which schedule data to use
    if (schedule.FullScheduleData.OAFullScheduleJsonData) {
        scheduleDataObj = schedule.FullScheduleData.OAFullScheduleJsonData;
    } else if (schedule.FullScheduleData.ISGSFullScheduleJsonData) {
        if (schedule.FullScheduleData.ISGSFullScheduleJsonData.ISGSThermalFullScheduleJsonData) {
            scheduleDataObj = schedule.FullScheduleData.ISGSFullScheduleJsonData.ISGSThermalFullScheduleJsonData;
        } else if (schedule.FullScheduleData.ISGSFullScheduleJsonData.ISGSHydroFullScheduleJsonData) {
            scheduleDataObj = schedule.FullScheduleData.ISGSFullScheduleJsonData.ISGSHydroFullScheduleJsonData;
        }
    }
    
    if (scheduleDataObj) {
        updateChart(scheduleDataObj);
        updateTable(scheduleDataObj);
    }
}

function updateChart(data) {
    const ctx = document.getElementById('scheduleChart').getContext('2d');
    
    if (currentChart) {
        currentChart.destroy();
    }
    
    const hours = Array.from({length: 96}, (_, i) => {
        const hour = Math.floor(i / 4);
        const quarter = (i % 4) * 15;
        return `${hour.toString().padStart(2, '0')}:${quarter.toString().padStart(2, '0')}`;
    });
    
    const datasets = [];
    
    if (data.SchdAmount || data.OnbarSchdAmount) {
        datasets.push({
            label: 'Scheduled Amount',
            data: data.SchdAmount || data.OnbarSchdAmount,
            borderColor: 'rgb(75, 192, 192)',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
        });
    }
    
    if (data.TotalInjBoundarySchdAmount) {
        datasets.push({
            label: 'Injection Boundary',
            data: data.TotalInjBoundarySchdAmount,
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
        });
    }
    
    if (data.TotalDrwBoundarySchdAmount) {
        datasets.push({
            label: 'Drawal Boundary',
            data: data.TotalDrwBoundarySchdAmount,
            borderColor: 'rgb(54, 162, 235)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
        });
    }
    
    // Get current theme for chart colors
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
    const isDark = currentTheme === 'dark';
    const textColor = isDark ? '#eee' : '#333';
    const gridColor = isDark ? '#4a5568' : '#e0e6ed';
    
    currentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: hours,
            datasets: datasets
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'MW (Instantaneous Power)',
                        color: textColor
                    },
                    ticks: {
                        color: textColor
                    },
                    grid: {
                        color: gridColor
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time (24 Hours - 15min intervals)',
                        color: textColor
                    },
                    ticks: {
                        color: textColor
                    },
                    grid: {
                        color: gridColor
                    }
                }
            },
            plugins: {
                title: {
                    display: true,
                    text: 'Hourly Schedule Data (MW per 15-minute block)',
                    color: textColor
                },
                legend: {
                    labels: {
                        color: textColor
                    }
                },
                tooltip: {
                    callbacks: {
                        afterLabel: function(context) {
                            return `Energy in this block: ${(context.parsed.y * 0.25).toFixed(3)} MWh`;
                        }
                    }
                }
            }
        }
    });
}

function updateTable(data) {
    const tbody = document.getElementById('hourly-data-body');
    tbody.innerHTML = '';
    
    const schedAmount = data.SchdAmount || data.OnbarSchdAmount || [];
    const injBoundary = data.TotalInjBoundarySchdAmount || [];
    const drwBoundary = data.TotalDrwBoundarySchdAmount || [];
    const pocInjLoss = data.POCInjectionLoss || [];
    const pocDrwLoss = data.POCDrawalLoss || [];
    
    for (let i = 0; i < Math.max(schedAmount.length, 96); i++) {
        const hour = Math.floor(i / 4);
        const quarter = (i % 4) * 15;
        const timeStr = `${hour.toString().padStart(2, '0')}:${quarter.toString().padStart(2, '0')}`;
        
        const scheduledMW = schedAmount[i] !== undefined ? schedAmount[i] : 0;
        const energyMWh = scheduledMW * 0.25; // Convert 15-min MW block to MWh
        
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${timeStr}</td>
            <td>${schedAmount[i] !== undefined ? schedAmount[i].toFixed(2) : 'N/A'}</td>
            <td>${schedAmount[i] !== undefined ? energyMWh.toFixed(3) : 'N/A'}</td>
            <td>${injBoundary[i] !== undefined ? injBoundary[i].toFixed(2) : 'N/A'}</td>
            <td>${drwBoundary[i] !== undefined ? drwBoundary[i].toFixed(2) : 'N/A'}</td>
            <td>${pocInjLoss[i] !== undefined ? pocInjLoss[i].toFixed(3) : 'N/A'}</td>
            <td>${pocDrwLoss[i] !== undefined ? pocDrwLoss[i].toFixed(3) : 'N/A'}</td>
        `;
        tbody.appendChild(row);
    }
}

function setupInitialChart() {
    // Show chart with first available schedule
    const firstGroup = scheduleData.ResponseBody.GroupWiseDataList[0];
    if (firstGroup && firstGroup.FullschdList && firstGroup.FullschdList[0]) {
        displayScheduleDetails(0, 0);
    }
}

function showTab(tabName) {
    // Hide all tab contents
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    
    // Remove active class from all tabs
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });
    
    // Show selected tab content
    document.getElementById(tabName).classList.add('active');
    
    // Add active class to clicked tab
    event.target.classList.add('active');
}