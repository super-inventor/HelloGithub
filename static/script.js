// 主题切换功能
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;
    
    // 检查本地存储中的主题偏好
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-theme');
        themeToggle.textContent = '切换到浅色';
    }
    
    // 主题切换事件
    themeToggle.addEventListener('click', function() {
        body.classList.toggle('dark-theme');
        
        if (body.classList.contains('dark-theme')) {
            themeToggle.textContent = '切换到浅色';
            localStorage.setItem('theme', 'dark');
        } else {
            themeToggle.textContent = '切换到深色';
            localStorage.setItem('theme', 'light');
        }
    });
    
    // 获取API消息
    fetch('/api/message')
        .then(response => response.json())
        .then(data => {
            console.log('API Response:', data);
        })
        .catch(error => {
            console.error('Error fetching message:', error);
        });
});
