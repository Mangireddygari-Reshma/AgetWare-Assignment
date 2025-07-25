import express from 'express';
import cors from 'cors';
import routes from './routes/index.js';
import { initDb, clearDb } from './db.js';

const app = express();
const PORT = 4000;

app.use(cors());
app.use(express.json());

app.get('/api/v1/health', (req, res) => {
  res.json({ status: 'ok' });
});

app.use('/api/v1', routes);

// Development-only: clear the database
if (process.env.NODE_ENV !== 'production') {
  app.post('/api/v1/dev/clear-db', async (req, res) => {
    await clearDb();
    res.json({ message: 'Database cleared.' });
  });
}

initDb().then(() => {
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}); 