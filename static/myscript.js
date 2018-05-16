var url_init = '_init'
var url_ran = '_random_numbers'
var column = [0, 0, 0]
var i = [1, 1, 1]

var data1 = { socket : 1 }
var data2 = { socket : 2 }
var data3 = { socket : 3 }

function start(){

    function column(data, i){

        column[i] = data.result

    }   

    $.getJSON(url_init, data1, function(data){ column(data, 0) })
    $.getJSON(url_init, data2, function(data){ column(data, 1) })
    $.getJSON(url_init, data3, function(data){ column(data, 2) })

    function loop(number){

        machine(url_ran, number)
        setTimeout(function() {

            if (i[number] <= column[number]) {

                i[number]++
                loop(number)

            }else 
                
                i[number] = 1

        }, 100) // 0.1 second

    }

    loop(0)
    loop(1)
    loop(2)

}

function machine(url, number){

    function show(data){

        var img = 'img' + number

        if(data.result == '1')

            document.getElementById(img).src = "/static/img/A.jpg";

        else if(data.result == '2')

            document.getElementById(img).src = "/static/img/B.jpg";

        else if(data.result == '3')

            document.getElementById(img).src = "/static/img/C.jpg";

        else if(data.result == '4')

            document.getElementById(img).src = "/static/img/D.jpg";

        else if(data.result == '5')

            document.getElementById(img).src = "/static/img/F.jpg";

    }

    $.getJSON(url, null, function(data){ show(data) })

}

window.onload = function(){

    document.getElementById("img0").src = "/static/img/F.jpg";
    document.getElementById("img1").src = "/static/img/F.jpg";
    document.getElementById("img2").src = "/static/img/F.jpg"; 
    
}