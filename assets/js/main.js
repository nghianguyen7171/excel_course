// Mobile menu toggle
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const mainNav = document.getElementById('main-nav');
    
    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            this.classList.toggle('active');
        });
    }
    
    // Smooth scrolling for anchor links
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);
                
                if (targetElement) {
                    const headerOffset = 80;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;
                    
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (mainNav.classList.contains('active')) {
                        mainNav.classList.remove('active');
                        mobileMenuToggle.classList.remove('active');
                    }
                }
            }
        });
    });
    
    // Highlight active section in navigation
    const sections = document.querySelectorAll('section[id], .section[id]');
    const navLinksArray = Array.from(navLinks);
    
    function highlightNavigation() {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.getBoundingClientRect().top;
            const sectionHeight = section.clientHeight;
            if (sectionTop <= 100 && sectionTop + sectionHeight > 100) {
                current = section.getAttribute('id');
            }
        });
        
        navLinksArray.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });
    }
    
    window.addEventListener('scroll', highlightNavigation);
    highlightNavigation();
    
    // Add scroll effect to header
    const siteHeader = document.getElementById('site-header');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            siteHeader.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
        } else {
            siteHeader.style.boxShadow = '0 1px 2px 0 rgba(0, 0, 0, 0.05)';
        }
        
        lastScroll = currentScroll;
    });
    
    // Quiz functionality
    const quizForm = document.getElementById('quiz-form');
    if (quizForm) {
        const submitButtons = document.querySelectorAll('.quiz-submit-btn');
        const quizCards = document.querySelectorAll('.quiz-card');
        
        // Handle answer selection
        const radioInputs = document.querySelectorAll('.quiz-option input[type="radio"]');
        radioInputs.forEach(input => {
            input.addEventListener('change', function() {
                const card = this.closest('.quiz-card');
                const submitBtn = card.querySelector('.quiz-submit-btn');
                if (!card.classList.contains('submitted')) {
                    submitBtn.disabled = false;
                    submitBtn.classList.add('enabled');
                }
            });
        });
        
        // Handle submit button clicks
        submitButtons.forEach(button => {
            button.disabled = true;
            button.addEventListener('click', function() {
                const questionNum = this.getAttribute('data-question');
                const card = this.closest('.quiz-card');
                const selectedInput = card.querySelector('input[type="radio"]:checked');
                const correctAnswer = card.getAttribute('data-correct');
                const answerDiv = document.getElementById(`answer-${questionNum}`);
                
                if (!selectedInput) {
                    alert('Please select an answer before submitting.');
                    return;
                }
                
                const selectedValue = selectedInput.value;
                const isCorrect = selectedValue === correctAnswer;
                
                // Mark card as submitted
                card.classList.add('submitted');
                if (isCorrect) {
                    card.classList.add('correct');
                } else {
                    card.classList.add('incorrect');
                }
                
                // Disable all radio buttons in this question
                const allInputs = card.querySelectorAll('input[type="radio"]');
                allInputs.forEach(input => input.disabled = true);
                
                // Disable submit button
                this.disabled = true;
                this.textContent = 'Submitted';
                this.classList.remove('enabled');
                
                // Show answer
                if (answerDiv) {
                    answerDiv.style.display = 'block';
                }
                
                // Highlight correct answer
                const correctOption = card.querySelector(`input[type="radio"][value="${correctAnswer}"]`);
                if (correctOption) {
                    const correctLabel = correctOption.closest('.quiz-option');
                    correctLabel.classList.add('correct-answer');
                }
                
                // Highlight selected answer if incorrect
                if (!isCorrect) {
                    const selectedLabel = selectedInput.closest('.quiz-option');
                    selectedLabel.classList.add('incorrect-answer');
                }
            });
        });
    }
});

