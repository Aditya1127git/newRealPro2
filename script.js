const slides = document.querySelectorAll(".slide");
let currentSlide = 0;
const next = document.querySelector("#next");
const prev = document.querySelector("#prev");
console.log(slides);
console.log(next);
console.log(prev);

function showSlide(index){
    slides.forEach(function(slide){
        slide.classList.remove("active");
    });
    slides[index].classList.add("active");
}
showSlide(currentSlide);
next.addEventListener("click", function(){
    nextSlide();
});
prev.addEventListener("click",function(){
    prevSlide();
});

setInterval(function(){
    nextSlide();
},4000);


function nextSlide(){
    currentSlide++;
    if(currentSlide >= slides.length){
        currentSlide = 0;
    }
    showSlide(currentSlide);
}

function prevSlide(){
    currentSlide--;
    if(currentSlide < 0){
        currentSlide = slides.length - 1;
    }
    showSlide(currentSlide);
}

const categoryCards = document.querySelectorAll('.course-category-card');
categoryCards.forEach(function(card){
    const toggle = card.querySelector('.course-toggle');
    if(toggle){
        toggle.addEventListener('click', function(){
            const isOpen = card.classList.contains('is-open');
            categoryCards.forEach(function(item){
                item.classList.remove('is-open');
                const itemToggle = item.querySelector('.course-toggle');
                if(itemToggle){
                    itemToggle.textContent = 'Read More';
                    itemToggle.setAttribute('aria-expanded', 'false');
                }
            });
            if(!isOpen){
                card.classList.add('is-open');
                toggle.textContent = 'Hide';
                toggle.setAttribute('aria-expanded', 'true');
            }
        });
    }
});

