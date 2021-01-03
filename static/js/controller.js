function gettime(){
    $.ajax({
        url:"/time",
        timeout: 10000, //设置超时时间为10秒
        success:function(data){
            $("#time").html(data);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

function get_c1_data(){
    $.ajax({
        url:"/c1",
        success:function(data){
            $(".num h1").eq(0).text(data.confirm);
            $(".num h1").eq(1).text(data.suspect);
            $(".num h1").eq(2).text(data.heal);
            $(".num h1").eq(3).text(data.dead);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

function get_c2_data(){
    $.ajax({
        url:"/c2",
        success:function(d){
            ec_center_option.series[0].data=d.data;
            ec_center.setOption(ec_center_option);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

function get_r1_data(){
    $.ajax({
        url:"/r1",
        success:function(data){
            ec_right1_option.xAxis[0].data = data.city;
            ec_right1_option.series[0].data = data.confirm;
            ec_right1.setOption(ec_right1_option);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

function get_l1_data(){
    $.ajax({
        url:"/l1",
        success:function(data){
            ec_left1_option.xAxis.data = data.date;
            ec_left1_option.series[0].data = data.confirm;
            ec_left1.setOption(ec_left1_option);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

function get_l2_data(){
    $.ajax({
        url:"/l2",
        success:function(data){
            ec_left2_option.xAxis.data = data.date;
            ec_left2_option.series[0].data = data.heal;
            ec_left2_option.series[1].data = data.dead;
            ec_left2.setOption(ec_left2_option);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

function get_r2_data(){
    $.ajax({
        url:"/r2",
        success:function(data){
            console.log(data.kws)
            ec_right2_option.list = data.kws
            WordCloud(ec_right2, ec_right2_option);
        },
        error:function(xhr,type,errorThrown){
        }
    })
}

gettime();
get_c1_data();
get_c2_data();
get_r1_data();
get_r2_data();
get_l1_data();
get_l2_data();

