1. Clone the Repository
```bash
git clone https://github.com/IvanStored/the_Spy_Cat_Agency.git
cd spy-cat-agency
```
2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Run app
```bash
main.py 
```

[Postman collection](https://www.postman.com/security-operator-14212269/spy-cat-agency/overview)

Bugs:

- Targets are not shown at the endpoint for all missions.
- Target status is updated but not shown in the response when updating target status.