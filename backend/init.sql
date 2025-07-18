-- Initial database setup
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_refresh_tokens_user_id ON refresh_tokens(user_id);
CREATE INDEX IF NOT EXISTS idx_refresh_tokens_expires_at ON refresh_tokens(expires_at);
CREATE INDEX IF NOT EXISTS idx_login_attempts_email ON login_attempts(email);
CREATE INDEX IF NOT EXISTS idx_login_attempts_attempted_at ON login_attempts(attempted_at);