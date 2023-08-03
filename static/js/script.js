window.addEventListener('DOMContentLoaded', function() {
    // Function to format time as HH:MM:SS
    function formatTime(timeInSeconds) {
      let hours = Math.floor(timeInSeconds / 3600);
      let minutes = Math.floor((timeInSeconds % 3600) / 60);
      let seconds = timeInSeconds % 60;

      return (
        (hours < 10 ? "0" : "") + hours + ":" +
        (minutes < 10 ? "0" : "") + minutes + ":" +
        (seconds < 10 ? "0" : "") + seconds
      );
    }

    // Function to start the timer
    function startTimer(durationInSeconds) {
      let timerElement = document.getElementById("timer");
      let timeRemaining = durationInSeconds;

      // Update the timer every second
      let interval = setInterval(function() {
        if (timeRemaining <= 0) {
          clearInterval(interval);
          timerElement.textContent = "Time's up!";
          // Automatically submit the form when time's up
          document.getElementById("quizForm").submit();
        } else {
          timerElement.textContent = formatTime(timeRemaining);
          timeRemaining--;
        }
      }, 1000);
    }

    // Get the total number of questions from the input field
   

    // Set the duration in seconds (e.g., 10 minutes = 10 * 60 seconds)
    const durationInSeconds = totalQuestionsCount * 60;

    // Start the timer
    startTimer(durationInSeconds);

    console.log(totalQuestionsCount);
  });