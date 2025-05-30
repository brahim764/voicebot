const express = require('express');
const { createEvent } = require('./googleCalendar');

const app = express();
app.use(express.json());

app.post('/voice', async (req, res) => {
  // Exemple basique : créer un RDV immédiatement
  const now = new Date();
  const end = new Date(now.getTime() + 30 * 60000); // 30 min

  await createEvent("Rendez-vous Clinique", now.toISOString(), end.toISOString());

  res.json({
    commands: [
      { say: { text: "Votre rendez-vous a été pris avec succès." } }
    ]
  });
});

app.listen(process.env.PORT || 3000, () => {
  console.log("Voicebot prêt avec intégration Google Calendar");
});
