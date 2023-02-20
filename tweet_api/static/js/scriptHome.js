
$(document).ready(function(){
    loadTweets();
})

function loadTweets(){
    const tweetsElement = document.getElementById("tweets");
 
    const xhr = new XMLHttpRequest();
    const method = 'GET';
    const url = "/tweet";
    const responseType = "json";

    // change how tweet appears in the page
    function formatTweet(tweet){
        var d = new Date(tweet.dateCreated)
        var ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d);
        var mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d);
        var da = new Intl.DateTimeFormat('en', { day: 'numeric' }).format(d);
        var date = `${da}/${mo}/${ye}`
        var currentTweet = "<h3>" + "tweet ke-" + tweet.id + " pada app ini" + "</h3>" + "<h6>" + tweet.content  +"</h6>" + "<p>" + date + "</p>";
        return currentTweet
    }

    console.log(url)

    xhr.responseType = responseType;
    xhr.open(method,url)
    xhr.onload = function() {
        console.log(xhr.response)
        const serverResponse = xhr.response
        var listedTweets = serverResponse.response
        console.log(listedTweets)
        var finalTweetStr = "";
        for(let i of listedTweets){
            var tweetObj = i;
            
            var formattedTweet = formatTweet(tweetObj);
            finalTweetStr += formattedTweet;
        }
        tweetsElement.innerHTML = finalTweetStr;

    }

    xhr.send()
}

// $(document).on('submit','#post-tweet-form',function(e){
//     console.log('tombol submit dipencet')
//     $.ajax({
//         method:"POST",
//         url:"/create-tweet/",
        
//         data:$('#post-create-tweet').serialize(),
            
//         dataType: "json",
//         success:function(){
//             console.log('Berhasil')
//             loadTweets();
//         }
//     })
// })