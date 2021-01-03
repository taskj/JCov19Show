var ec_right2 = document.getElementById('r2');
var ec_right2_option = {
        "list": "",//或者[['各位观众',45],['词云', 21],['来啦!!!',13]],只要格式满足这样都可以
        "gridSize": 1, // 密集程度 数字越小越密集
        "weightFactor": 0.0001, // 字体大小=原始大小*weightFactor
        "maxFontSize": 100, //最大字号
        "minFontSize": 1, //最小字号
        "fontWeight": 'normal', //字体粗细
        "fontFamily": 'Times, serif', // 字体
        "color": 'random-light', // 字体颜色 'random-dark' 或者 'random-light'
        "backgroundColor": '#333', // 背景颜色
        "rotateRatio": 1, // 字体倾斜(旋转)概率，1代表总是倾斜(旋转)
        "backgroundColor": "#15122A"
    };
//WordCloud(ec_right2, ec_right2_option);