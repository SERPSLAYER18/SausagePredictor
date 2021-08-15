import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";
import {useState} from "react";

export const Example = () => {
    const [startDate, setStartDate] = useState(new Date());
    return (
        <DatePicker selected={startDate} onChange={(date) => setStartDate(date.toISOString().slice(0, 10))} />
    );
};