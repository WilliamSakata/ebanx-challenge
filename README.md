# Ebanx-challenge

This is a project developed to the Ebanx challenge.

This project is developed using Python and the FastAPI framework.

To run this project execute the following commands:

```bash
pip install requirenments.txt
fastapi dev src/main.py
```

The endpoints implemented are:

**POST**

```
/reset
```

Used to clean the application data.

Response:

```
HTTP 200
```

---

**GET**

```
/balance?account_id=100
```

Used to get balance from a specific account

Response:

```
HTTP 200
20
```

```
HTTP 404
0
```

---

**POST**

```
/event
```

Used to execute a certain use case. The valid use cases are:

- Deposit
- Withdraw
- Transfer

### **Deposit**

Payload

```
{"type":"deposit", "destination":"100", "amount":10}
```

Response

```
HTTP 201
{"destination":{"id":"100","balance":10}}
```

### **Withdraw**

Payload

```
{"type":"withdraw", "origin":"100", "amount":5}
```

Response

```
HTTP 201
{"origin": {"id":"100", "balance":15}}
```

### **Transfer**

Payload

```
{"type":"transfer", "origin":"100", "amount":15, "destination":"300"}
```

Response

```
HTTP 201
{"origin": {"id":"100", "balance":0}, "destination": {"id":"300", "balance":15}}
```
