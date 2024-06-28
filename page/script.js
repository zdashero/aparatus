$(document).ready(function() {
    $.getJSON('https://api.ipify.org?format=json', function(data) {
        const ip = data.ip;
        const text = `Enjoy ${ip} Don't Forget To Star My Repos`;
        let i = 0;
        const speed = 100;
        let isDeleting = false;
        let isTyping = true;

        function typeWriter() {
            if (isTyping) {
                if (i < text.length) {
                    document.getElementById("typing").innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, speed);
                } else {
                    isTyping = false;
                    setTimeout(() => { isDeleting = true; typeWriter(); }, 1000);
                }
            } else if (isDeleting) {
                if (i >= 0) {
                    document.getElementById("typing").innerHTML = text.substring(0, i);
                    i--;
                    setTimeout(typeWriter, speed);
                } else {
                    isDeleting = false;
                }
            }
        }

        typeWriter();
    });
});
