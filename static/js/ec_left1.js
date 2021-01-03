var ec_left1 = echarts.init(document.getElementById("l1"),"dark");
var ec_left1_option = {
    title: {
        text: '确诊人数'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: [""]
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: [""]
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '确诊人数',
            type: 'line',
            stack: '总量',
            data: [""]
        },
        {
            name: '确诊人数',
            type: 'line',
            stack: '总量',
            data: []
        }
    ]
};
ec_left1.setOption(ec_left1_option);