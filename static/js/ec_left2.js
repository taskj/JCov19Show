var ec_left2 = echarts.init(document.getElementById("l2"),"dark");
var ec_left2_option = {
    title: {
        text: '治愈/死亡人数'
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: ["治愈人数","死亡人数"]
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
            name: '死亡人数',
            type: 'line',
            stack: '总量',
            data: [""]
        },
        {
            name: '治愈人数',
            type: 'line',
            stack: '总量',
            data: []
        }
    ]
};
ec_left2.setOption(ec_left2_option);