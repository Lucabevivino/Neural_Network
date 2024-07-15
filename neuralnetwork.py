class NeuralNetwork:

# questo attributo definisce la dimensione (numeero di nodi o neuroni) dello strato nascosto

    
    def __init__(self, hidden_layer_size = 100):
        
        self.hidden_layer_size = hidden_layer_size
    
# La seguente funzione (metrica)'accuracy' esrpime l'accuratezza delle previsoni del codice confrontandole con un dataset. Utilizza la vettorizzazione di Numpy, ovvero esegue l'operazione y == y_pred che produce un vettore composto da 1 nelle posizioni dove c'è corrispondenza tra y e y_pred e zero altrimenti, poi esegue la somma di tutti i valori (numero di corrispondenze) e divide per il numero di osservazioni (ottenimao la media). Il problema di questa tecnica è che da a tutti gli errori lo stesso valore (un errore grossolano pesa qunato un errore minore)   
    
    def _accuracy(self, y,y_pred):            
        
        return np.sum(y == y_pred) / len(y)    
        
# Affianchiamo ad accuracy la funzione log loss che aiuta proprio a pesare gli errori. La funzione è definita come L(y, p) = -y * log(p) - (1 - y) * log(1 - p)
# Dove:

# L è la perdita entropica incrociata
# y è la vera etichetta di classe (1 per gatto, 0 per cane)
# p è la probabilità predetta dal modello che l'immagine appartenga alla classe 1 (gatto)     
# il risultato di tale funzione rappresenta quanto le predizioni di tale modello sono vicine ai dati reali
# np.dot realizza il prodotto scalare tra due vettori (sommatoria degli elementi nella stessa posizione)

    def _log_loss(self, y_true, y_proba):
        
        return -np.sum(np.dot(y_true, np.log(y_proba)) + np.dpt((1-y_true), np.log(1-y_proba)))/len(y_true)
        

# Ora bisogna inserire una funzione che stabilisca se creare una nuova connessione con un altro nodo (neurone) o no. Questa funzione generalmente si chiama funzione di attivazione, nello specifico elabora l'input e decide se bisogna generare un output. esistono diversi tipi di funzioni di attivazione, ognuna con il proprio modo di interpretare i dati in ingresso. Questo significa che possiamo creare neuroni con diverse funzioni di attivazione, quindi creare diversità tra i neuroni e quindi apprendere idversi tipi di informazioni e pattern nei dati. Ogni funzione esalta doverse caratteristiche del dato letto. Noi useremo due funzioni: 
# Rectified Linear Unit (ReLU) --> molto comune negli strati nascosti:
# Per ogni valore di input:
# Se il valore è positivo, la funzione ReLU restituisce il valore stesso. In altre parole, l'input non viene modificato.
# Se il valore è negativo, la funzione ReLU restituisce 0. In altre parole, il valore negativo viene azzerato.

    def _relu(self, Z):
        
        return np.maximum(Z, 0) 

# Sigmoide --> strati di output:
# La funzione sigmoide prende un valore in ingresso compreso tra -∞ e +∞ e lo trasforma in un valore in uscita compreso tra 0 e 1.
# Matematicamente, la funzione sigmoide è definita come: f(x) = 1 / (1 + e^(-x))

    def _sigmoid(self, Z):
        
        return 1/(1 + np.power(np.e, -Z))
# Forward Propagation:

    def _forward_propagation(self, X):
        
        Z1 = np.dot(X, W1) + b1
        
        A1 = relu(Z1)
        Z2 = np.dot(A1, W2) + b2
        A2 = sigmoid (Z2)

# È stata creata una cache per salvare i valori intermedi       
       
        self.cache = (Z1, A1, Z2,A2)

# Questa istruzione ci permette di trasformare A1 in un array monodimensionale      
        
        return A2.ravel()
        
# Ora bisogna creare l'ultimo strato che ritorna la probabilità che l'osservazione in input appartenga alla classe positiva, con una probabilità uguale o inferiore al 50% nsi ritiene positiva, se no, negativa

def predict(self, X):
    
    proba = self._forward_propagation(X)
    
    y = np.zeros(X.shape[0])
    y[proba >= 0.5] = 1
    y[proba < 0.5] = 0
    
    return y

def predict_proba(self, X):
    
    return self._forward_propagation(X)
    
        









        