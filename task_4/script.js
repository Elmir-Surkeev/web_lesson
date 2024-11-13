
function searchMovies() {
    const query = document.getElementById('searchInput').value;
    if (query) {
        alert(`Вы ищете: ${query}`);
    } else {
        alert("Пожалуйста, введите запрос для поиска.");
    }
}

// Функция для имитации входа
function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username && password) {
        alert(`Добро пожаловать, ${username}!`);
    } else {
        alert("Пожалуйста, введите логин и пароль.");
    }
}
