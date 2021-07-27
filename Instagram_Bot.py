from selenium import webdriver
import time
import datetime as dt
import random

philosophie = ("La philosophie est le microscope de la pensée. éd. J. Hetzel et A. Quantin, 1882, partie V, chap. 2, p. 162 - Victor Hugo, ",
                   "Le jardin, c’est de la philosophie rendue visible. Le Monde de l’Education, 07/2000, 283, p.12-17 - Erik Orsenna",
                   "La philosophie de l'artillerie : Cogito ergo boum. - Susan Sontag",
                   "La philosophie commence avec l'étonnement. Méthaphysique - Aristote",
                   "Notre philosophie ? Thèse, antithèse, charentaises. chronique Nous sommes tous des frilosophes - Vincent Roca",
                   "Toucher à la philosophie, c'est palper le coeur."
                   "Comenius ou combattre la pauvreté par l'éducation de tous - Jean Bédard",
                   "Toute philosophie est « critique du langage ». Tractatus logico-philosophicus, Ludwig Wittgenstein (trad. Gilles Gaston Granger), éd. Gallimard Tel, 1993 (ISBN 2-07-075864-8), p. 51 - Ludwig Wittgenstein",
                   "Le je fait son entrée dans la philosophie grâce à ceci : que le monde est mon monde. Tractatus logico-philosophicus, Ludwig Wittgenstein (trad. Gilles Gaston Granger), éd. Gallimard Tel, 1993 (ISBN 2-07-075864-8), p. 95 - Ludwig Wittgenstein",
                   "Croître pour croître est la philosophie du cancer. Délivrez-moi !, Jasper Fforde, éd. 10/18, 2002 (ISBN 2-264-04390-3), p. 116 - Jasper Fforde",
                   "ÉCLECTISME : Tonner contre comme étant une philosophie immorale. Dictionnaire des idées reçues - Gustave Flaubert",
                   "Dans les naïvetés d'un enfant bien né, il y a quelquefois une philosophie bien aimable. Maximes et Pensées - Chamfort",
                   "Dis-moi comment tu traites le présent et je te dirai quelle philosophie tu es. Note conjointe sur M. Descartes et la philosophie cartésienne Source : Note conjointe sur M. Descartes et la philosophie cartésienne - Charles Péguy",
                   "La philosophie est art de vivre, ou elle ne mérite pas une heure de peine. Le désir d'être un volcan - Michel Onfray",
                   "Platon trouva la philosophie faite de brique, et la fit d’or. Pensées (~1780-1824), Joseph Joubert, éd. Librairie Vve Le Normant, 1850, t. 2, p. 152 - Joseph Joubert",
                   "Soyez philosophe ; mais, au milieu de toute votre philosophie, soyez toujours un homme. Enquête sur l’entendement humain (1758), David Hume (trad. André Leroy), éd. Flammarion, 2006 (ISBN 2-08-071305-1), p. 51 - David Hume",
                   "Se moquer de la philosophie, c'est vraiment philosopher. Pensées. - Blaise Pascal",
                   "La philosophie est l'art de s'illusionner sur la vérité. Mes pensées profondes - Bertrand Vac",
                   "La philosophie compte parmi les plus originels des efforts humains. Qu’est-ce qu’une chose (1962), Martin Heidegger (trad. Jean Reboul et Jacques Taminiaux), éd. Gallimard, coll. Tel, 2006 (ISBN 2-07-071465-9), p. 69 - Martin Heidegger",
                   "La poésie contient la philosophie comme l'âme contient la raison. Post-scriptum de ma vie - Victor Hugo",
                   "La philosophie ne répond que des individus, mais la religion répond des masses. Oeuvres de rivarol: etudes sur sa vie et son esprit (édition 1852) - Antoine de Rivarol",
                   "La philosophie peut être mauvaise alors même que les poèmes sont beaux. La psychanalyse du feu - Gaston Bachelard",
                   "La philosophie est une affaire solitaire. Responsabilité et jugement, hannah arendt (trad. jean-luc fidel), éd. payot, 2003, p. 40 - responsabilité et jugement, 2003 - Hannah Arendt",
                   "Kama Sutra : philosophie du couple où l’on campe sur ses positions. Déconfitures et pas de pot - Editions Hélène Jacob - 2015 - - Kathy Dorl",
                   "Ma philosophie ne m'a rien rapporté, mais elle m'a beaucoup épargné. La vie, l'amour et la mort (édition 1897) - Arthur Schopenhauer",
                   "Le tort de la philosophie est d'être trop supportable. Syllogismes de l'amertume - Emil Cioran",
                   "Il n'y a rien en philosophie qui ne puisse se dire dans la langue de tout le monde. Revue de Paris 15 mai 1915 - Bergson",
                   "L'insecte, c'est une autre philosophie, un autre espace-temps, une autre dimension. Les fourmis - Bernard Werber",
                   "Ma philosophie de la cuisine : Cent fois sur le métier, remettez votre ouvrage. Best of Paul Bocuse par Paul Bocuse - Paul Bocuse",
                   "Un peu de philosophie écarte de la religion et beaucoup y ramène. Esprit de rivarol (édition 1808) - Antoine de Rivarol",
                   "Ma philosophie c'est : le présent n'existe pas. Seul le futur passe Les petits ruisseaux - Pascal Rabaté",
                   "La vraie philosophie est de voir les choses telles qu'elles sont. Oeuvres complètes de buffon: l'homme (édition 1818) - Georges-Louis Leclerc de Buffon")

randomnumberphilo = random.randint(0, 31)
print(philosophie[randomnumberphilo])

DATE = dt.datetime.now()
string_date = DATE.strftime("%A, %d %B, %y")
driver = webdriver.Chrome(executable_path="/app/.chromedriver/bin/chromedriver")

pseudo = random.randrange(0, 101, 2)
print(pseudo)

driver.get("https://www.instagram.com/")
time.sleep(10)
driver.find_elements_by_xpath("/html/body/div[3]/div/div/button[1]").click()time.sleep(10)
A1 = driver.find_elements_by_name("username")[0].send_keys('yoschigamer57@gmail.com')
A1 = driver.find_elements_by_name("password")[0].send_keys('kiki57660')

A1 = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0].click()
time.sleep(10)
A1 = driver.find_elements_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')[0].click()
time.sleep(10)

driver.get('https://www.instagram.com/accounts/edit/')

A1 = driver.find_elements_by_class_name("p7vTm")[0].clear()

A1 = driver.find_elements_by_class_name("p7vTm")[0].send_keys(f'(we are the 20 {string_date} ) <> {philosophie[randomnumberphilo]}')

A1 = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/article/form/div[11]/div/div/button')[0].click()
