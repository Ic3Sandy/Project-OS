var url_init = '_init'
var url_ran = '_random_numbers'
var column = [0, 0, 0]
var i = [1, 1, 1]

var token = 0
var check_reward = ['', '', '']

// Assign dictionary
var data1 = { socket : 1 }
var data2 = { socket : 2 }
var data3 = { socket : 3 }

function start(){

    if(token == 0)
        return
    else
        token--

    document.getElementById("token").innerHTML = token

    // Assign data that receive from server
    function column(data, i){ column[i] = data.result }   

    // Get JSON data from server by url and run column function
    $.getJSON(url_init, data1, function(data){ column(data, 0) })
    $.getJSON(url_init, data2, function(data){ column(data, 1) })
    $.getJSON(url_init, data3, function(data){ column(data, 2) })

    // Loop for display image
    function loop(number){

        machine(url_ran, number)

        // Display data after 0.1 second 
        setTimeout(function() {

            if (i[number] <= column[number]) {

                i[number]++
                loop(number)

            }else{

                if (number == 2){
                    
                    document.getElementById("token").innerHTML = token
                }

                i[number] = 1

            }
                
        }, 100) // 0.1 second

    }

    // Start loop that parallel work by thread
    loop(0)
    loop(1)
    loop(2)

}

// Display image from data that receive
function machine(url_ran, number){

    function show(data){

        var img = 'img' + number

        check_reward[number] = data.result

        if(data.result == 1)

            document.getElementById(img).src = "/static/img/A.jpg"

        else if(data.result == 2)

            document.getElementById(img).src = "/static/img/B.jpg"

        else if(data.result == 3)

            document.getElementById(img).src = "/static/img/C.jpg"

        else if(data.result == 4)

            document.getElementById(img).src = "/static/img/D.jpg"

        else if(data.result == 5)

            document.getElementById(img).src = "/static/img/F.jpg"

    }

    // Get JSON data from server by url and run show function    
    $.getJSON(url_ran, null, function(data){ show(data) })

}

// Display default image when window execute this page
window.onload = function(){

    token = 3
    document.getElementById("img0").src = "/static/img/F.jpg"
    document.getElementById("img1").src = "/static/img/F.jpg"
    document.getElementById("img2").src = "/static/img/F.jpg"
    document.getElementById("token").innerHTML = token
    
}