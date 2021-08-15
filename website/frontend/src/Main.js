import './Main.css';
import {useState} from "react";
import {Example} from "./DateChoose"
import DatePicker from "react-datepicker";

function Main() {
    const sendJSON = () => {
        const requestOptions = {
            method: 'POST',
            headers: {},
            body: JSON.stringify({
                "date": [startDate],
                "product_id": [product],
                "store_id": [address],
                "sales": [values],
            }),

        };

        fetch('http://192.168.1.34:8080/add', requestOptions)
            .then(response => response.json())
            .then(data => setResult(data['answer']));
    }
    const [product, setProduct] = useState("")
    const [address, setAddress] = useState("")
    const [values, setValues] = useState("")
    const [result, setResult] = useState(0)
    const [startDate, setStartDate] = useState(new Date());
    return (
        <div className="App">
            <div className="container">
                <div className="prikol">
                    <h3>Predict "Vitalur" demand</h3>

                    <fieldset>
                        <input className="kekw" placeholder="Product name" type="text" tabIndex="1" name="product_"
                               required autoFocus
                               onChange={(e) => {
                                   setProduct(e.target.value)
                               }}/>
                    </fieldset>
                    <fieldset>
                        <input className="kekw" placeholder="Store address" type="text" tabIndex="2" name="address_"
                               required
                               onChange={(e) => {
                                   setAddress(e.target.value)
                               }}/>
                    </fieldset>
                    <fieldset>
                        <input className="kekw" placeholder="Values" type="text" tabIndex="3" name="values_" required
                               onChange={(e) => {
                                   setValues(e.target.value)
                               }}/>
                    </fieldset>
                    <fieldset>
                        <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
                    </fieldset>
                    <fieldset>
                        <input className="kekw" placeholder="Prediction" type="text" tabIndex="3" name="values_"
                               disabled
                               value={result}/>
                    </fieldset>
                    <button id="main_button" className="button-5" role="button" onClick={sendJSON}>Predict!</button>
                    <p className="copyright">Designed by Team3</p>

                </div>
            </div>
        </div>
    );
}

export default Main;