// reckitt_app/static/reckitt_app/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Auto hide alerts after 5 seconds
    setTimeout(function() {
        const alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
    
    // Enable tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Confirmation for delete buttons with data-confirm attribute
    const confirmButtons = document.querySelectorAll('[data-confirm]');
    confirmButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (!confirm(this.dataset.confirm)) {
                e.preventDefault();
            }
        });
    });
    
    // Handle department filter changes
    const departmentFilter = document.getElementById('department-filter');
    if (departmentFilter) {
        departmentFilter.addEventListener('change', function() {
            this.closest('form').submit();
        });
    }
    
    // Preview image for URL inputs
    const pictureUrlInput = document.getElementById('id_picture_url');
    if (pictureUrlInput) {
        const previewContainer = document.createElement('div');
        previewContainer.classList.add('mt-2');
        previewContainer.style.display = 'none';
        
        const previewImage = document.createElement('img');
        previewImage.classList.add('rounded', 'shadow-sm');
        previewImage.style.maxHeight = '100px';
        
        previewContainer.appendChild(previewImage);
        pictureUrlInput.parentNode.appendChild(previewContainer);
        
        // Update preview when URL changes
        pictureUrlInput.addEventListener('input', function() {
            const url = this.value.trim();
            if (url) {
                previewImage.src = url;
                previewContainer.style.display = 'block';
                
                // Handle image load error
                previewImage.onerror = function() {
                    previewContainer.style.display = 'none';
                };
            } else {
                previewContainer.style.display = 'none';
            }
        });
        
        // Show preview on page load if URL exists
        if (pictureUrlInput.value.trim()) {
            previewImage.src = pictureUrlInput.value.trim();
            previewContainer.style.display = 'block';
        }
    }
});