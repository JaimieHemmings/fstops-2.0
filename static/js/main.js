document.addEventListener('DOMContentLoaded', function() {
  // Menu Toggle function
  let menuToggleBtn = document.getElementById('menu-burger');
  let menu = document.getElementById('nav-overlay');

  menuToggleBtn.addEventListener('click', function() {
    menu.classList.toggle('open');
  });

  // Testimonials Function
  let nextTestimonial = document.getElementById('testimonials-next');
  let prevTestimonial = document.getElementById('testimonials-prev');

  let currentTestimonial = 1;

  let testimonials = document.getElementById('testimonials-container').children;

  testimonials[0].classList.toggle('opacity-0');
  testimonials[0].classList.toggle('absolute');

  nextTestimonial.addEventListener('click', function() {
    currentTestimonial++;
    updateTestimonial();
  });

  prevTestimonial.addEventListener('click', function() {
    currentTestimonial--;
    updateTestimonial();
  });

  function updateTestimonial() {
    if (currentTestimonial > testimonials.length) {
      currentTestimonial = 1;
    } else if (currentTestimonial < 1) {
      currentTestimonial = testimonials.length;
    }

    for (let i = 0; i < testimonials.length; i++) {
      testimonials[i].classList.add('opacity-0');
      testimonials[i].classList.add('absolute');
    }

    testimonials[currentTestimonial - 1].classList.remove('opacity-0');
    testimonials[currentTestimonial - 1].classList.remove('absolute');
  }
});