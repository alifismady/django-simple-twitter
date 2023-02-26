
$(document).ready(function(){
    loadTweets();
})


function loadTweets(){
    const tweetsElement = document.getElementById("tweets");
 
    const xhr = new XMLHttpRequest();
    const method = 'GET';
    const url = "/tweet";
    const responseType = "json";
    console.log(url)

    xhr.responseType = responseType;
    xhr.open(method,url)
    xhr.onload = function() {
        console.log(xhr.response)
        const serverResponse = xhr.response
        var listedTweets = serverResponse
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


var userName = document.getElementById("userName").value;
console.log(userName)

// change how tweet appears in the page
function formatTweet(tweet){
    
    var d = new Date(tweet.dateCreated)
    var ye = new Intl.DateTimeFormat('en', { year: 'numeric' }).format(d);
    var mo = new Intl.DateTimeFormat('en', { month: 'short' }).format(d);
    var da = new Intl.DateTimeFormat('en', { day: 'numeric' }).format(d);
    var date = `${da}/${mo}/${ye}`
    if(userName == tweet.username){
        var cardReturn = `
    <div class="tweetcard card shadow p-3 mb-5 bg-body-tertiary rounded border-0">
        <div class="card-body">
            <blockquote class="blockquote mb-0">
            <a class="btn" style="float:right;" href="delete/${tweet.id}" role="button"><i class="bi bi-trash" style="color:#D11A2A"></i></a>
            <a class="btn" style="float:right;" role="button" id="button${tweet.id}" onclick="openModal(${tweet.id})"><i class="bi bi-pencil-square" style="color:#ffffff"></i></a>
            <h4>@${tweet.username}</h4>
            <p>${tweet.content}</p>
            <footer class="blockquote-footer" id="tweetDate">Tweeted on ${date}</footer>
            </blockquote>
        </div>
    </div>
    `
    } else {
        var cardReturn = `
        <div class="tweetcard card shadow p-3 mb-5 bg-body-tertiary rounded border-0">
            <div class="card-body">
                <blockquote class="blockquote mb-0">
                <h4>@${tweet.username}</h4>
                <p>${tweet.content}</p>
                <footer class="blockquote-footer" id="tweetDate">Tweeted on ${date}</footer>
                </blockquote>
            </div>
        </div>
        `
    }
    
    return cardReturn
}

function openModal(tweet_id){
    $('#tweetModal').modal('show')
    document.getElementById('post-tweet-form').setAttribute("action","/update/"+tweet_id)

}

