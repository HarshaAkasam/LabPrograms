// login.js - export User class (ES module)
export class User {
  validate(username, password) {
    if (username === password) return 'Login Successful';
    return 'Unauthorized access';
  }
}
