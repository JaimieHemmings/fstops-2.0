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

  // Add event listener to items with the class faq-toggle
  let faqItems = document.querySelectorAll('.faq-toggle');

  faqItems.forEach(function(item) {
    item.addEventListener('click', function() {
      let index = parseInt(item.getAttribute('data-index'));
      toggleAccordion(index);
    });
  });

  // Accordion Function
  function toggleAccordion(index) {
    // close all other accordion tabs
    for (let i = 1; i <= faqItems.length; i++) {
      if (i !== index) {
        const content = document.getElementById(`content-${i}`);
        const icon = document.getElementById(`icon-${i}`);
        content.style.maxHeight = '0';
        icon.innerHTML = `
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
            <path d="M8.75 3.75a.75.75 0 0 0-1.5 0v3.5h-3.5a.75.75 0 0 0 0 1.5h3.5v3.5a.75.75 0 0 0 1.5 0v-3.5h3.5a.75.75 0 0 0 0-1.5h-3.5v-3.5Z" />
          </svg>
        `;
      }
    }
    const content = document.getElementById(`content-${index}`);
    const icon = document.getElementById(`icon-${index}`);
 
    // SVG for Minus icon
    const minusSVG = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
        <path d="M3.75 7.25a.75.75 0 0 0 0 1.5h8.5a.75.75 0 0 0 0-1.5h-8.5Z" />
      </svg>
    `;
 
    // SVG for Plus icon
    const plusSVG = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" class="w-4 h-4">
        <path d="M8.75 3.75a.75.75 0 0 0-1.5 0v3.5h-3.5a.75.75 0 0 0 0 1.5h3.5v3.5a.75.75 0 0 0 1.5 0v-3.5h3.5a.75.75 0 0 0 0-1.5h-3.5v-3.5Z" />
      </svg>
    `;
 
    // Toggle the content's max-height for smooth opening and closing
    if (content.style.maxHeight && content.style.maxHeight !== '0px') {
      content.style.maxHeight = '0';
      icon.innerHTML = plusSVG;
    } else {
      content.style.maxHeight = content.scrollHeight + 'px';
      icon.innerHTML = minusSVG;
    }
  }
  

});