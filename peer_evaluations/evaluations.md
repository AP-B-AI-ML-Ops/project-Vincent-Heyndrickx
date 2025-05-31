# Peer evaluations MLOps

---

## Peer eval 1: Mauro De Mey

| Onderdeel project        | Punt | Motivatie |
|--------------------------|------|------------|
| **Problem Description**   | 2    | Het probleem werd goed omschreven. De keuze van de dataset werd duidelijk uitgelegd. De flows en wat ze stap voor stap doen is ook duidelijk en volledig. Hoe het project moet worden gerund staat ook duidelijk beschreven van de eerste tot de laatste stap. |
| **Experiment tracking & model registry** | 2 | Onder de map `train` staat de file `register.py` die het model correct registreert in de mlflow register. Experiment tracking gebeurt ook correct en is containerized. |
| **Workflow orchestration** | 2 | De workflow is volledig uitgewerkt in de code. Prefect server wordt ook in een container gedraaid. |
| **Model deployment** | 2 | Een container voert een script uit voor prefect, dit script voert dan de deployment python file uit. Het voert automatisch uit met de dockerfile. |
| **Model monitoring** | 1 | Er is wel monitoring met evidently en een grafana dashboard. Echter ik vond geen scripts om alerts of voorwaardelijke flows te runnen. |
| **Reproducibility** | 2 | Alles werd goed uitgelegd hoe je het project moet runnen, alles start op zoals het hoort. Er werd ook een voorbeeld .env gegeven. |

---

## Peer eval 2: Loic Van Camp

| Onderdeel project        | Punt | Motivatie |
|--------------------------|------|------------|
| **Problem Description**   | 2    | Er wordt goed uitgelegd welke dataset gebruikt wordt en hoe deze gesplit wordt. Het is ook duidelijk waarvoor het project dient en de flows zijn duidelijk uitgeschreven met uitleg. |
| **Experiment tracking & model registry** | 2 | Als ik de code bekijk zou de experiment tracking en model registry horen te werken. Er is een script voor zowel tracking als registry. |
| **Workflow orchestration** | 2 | Workflow is helemaal uitgewerkt in alle files. |
| **Model deployment** | 2 | Model is gedeployt en containerized. Het kan naar de cloud gedeployt worden. |
| **Model monitoring** | 2 | Model monitoring is volledig uitgewerkt en geeft alerts bij data drift. |
| **Reproducibility** | 1 | De uitleg hoe de code moet runnen is er. Het lukt me niet het runnende te krijgen. Alle containers starten en geven dan een fout van een map die niet zou bestaan. |

---

## Peer eval 3: Kaan Sekerci

| Onderdeel project        | Punt | Motivatie |
|--------------------------|------|------------|
| **Problem Description**   | 2    | Het probleem staat mooi omschreven met uitleg van de technologie dat gebruikt werd en zelfs de mappenstructuur van het project. Het is helemaal duidelijk waar het project voor is bedoeld. |
| **Experiment tracking & model registry** | 2 | Model werd correct opgeslagen en ik kon alles bijhouden in prefect en mlflow. MLflow werkt perfect. |
| **Workflow orchestration** | 2 | De workflow is helemaal uitgewerkt en werkt zoals verwacht. |
| **Model deployment** | 2 | Model kan gedeployt worden en is containerized. |
| **Model monitoring** | 1 | Er is monitoring dat reports genereert. Geen alerts of extra runs als metric threshold overschreden wordt. |
| **Reproducibility** | 1 | Er is wel een uitleg van hoe je alles moet uitvoeren, als je de instructies volgt kom je wel direct op een groot probleem. Je krijgt een foutmelding dat docker een .env file zoekt die niet bestaat, er staat ook nergens beschreven hoe je deze moet aanmaken. Na verder te zoeken is er wel een voorbeeld in de code zelf, maar dit staat niet duidelijk vermeld in de README van het project. |
