const rotatingWords = ["Home", "Office", "Shop", "Business"];
const changingText = document.getElementById("changingText");
let wordIndex = 0;

if (changingText) {
    setInterval(() => {
        wordIndex = (wordIndex + 1) % rotatingWords.length;
        changingText.textContent = rotatingWords[wordIndex];
    }, 2000);
}

const counters = document.querySelectorAll(".counter");

counters.forEach(counter => {
    const target = +counter.getAttribute("data-target");
    let count = 0;
    const speed = Math.max(10, Math.floor(2000 / target));

    const updateCounter = () => {
        if (count < target) {
            count++;
            counter.textContent = count + "+";
            setTimeout(updateCounter, speed);
        } else {
            counter.textContent = target + "+";
        }
    };

    updateCounter();
});

const sections = document.querySelectorAll("section[id]");
const navLinks = document.querySelectorAll(".nav-link");

window.addEventListener("scroll", () => {
    let current = "";

    sections.forEach(section => {
        const sectionTop = section.offsetTop - 120;
        const sectionHeight = section.offsetHeight;

        if (window.pageYOffset >= sectionTop && window.pageYOffset < sectionTop + sectionHeight) {
            current = section.getAttribute("id");
        }
    });

    navLinks.forEach(link => {
        link.classList.remove("active");
        if (link.getAttribute("href") === `#${current}`) {
            link.classList.add("active");
        }
    });
});