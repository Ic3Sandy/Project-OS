var url_init = '_init'
var url_ran = '_random_numbers'
var column = [0, 0, 0]
var i = [1, 1, 1]

var token = 0
var check_reward = [0, 0, 0]
var working = false

// Assign dictionary
var data1 = { socket : 1 }
var data2 = { socket : 2 }
var data3 = { socket : 3 }

function start(){

    if(token == 0 || working)
        return
    else{
        token--
        working = true
    }
        

    document.getElementById("token").innerHTML = token

    // Assign data that receive from server
    function column(data, i){ 
        column[i] = data.result

        if(i == 2){
            // Start loop that parallel work by thread
            loop(0)
            loop(1)
            loop(2)
        }

    }   

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
                // alert("i[number]: "+i[number]+" column[number]: "+column[number])
                if (number == 2)
                    check_rewards()

                i[number] = 1

            }
                
        }, 75) // 0.1 second

    }

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

function check_rewards(){


    if(check_reward[0] == 5 && check_reward[1] == 5 && check_reward[2] == 5){

        token+=10
        alert("You get a ten token!")

    }

    else if(check_reward[0] == 1 && check_reward[1] == 2 && check_reward[2] == 3){

        token+=7
        alert("You get a seven token!")

    }

    else if(check_reward[0] == check_reward[1] && check_reward[1] == check_reward[2]){

        token+=5
        alert("You get a five token!")

    }

    else if(check_reward[0] == check_reward[1] || check_reward[1] == check_reward[2]){

        token+=1
        alert("You get a one token!")

    }

    else alert("You have to try harder than this!")

    working = false

    document.getElementById("token").innerHTML = token

}

// Display default image when window execute this page
window.onload = function(){

    token = 3
    document.getElementById("img0").src = "/static/img/F.jpg"
    document.getElementById("img1").src = "/static/img/F.jpg"
    document.getElementById("img2").src = "/static/img/F.jpg"
    document.getElementById("token").innerHTML = token
    
}