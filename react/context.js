// app
import "./styles.css";
import ThemeContextProvider from "./Context";
import Result from "./Result";

import appReducers from './rootRuducer';


export default function App() {

  return (
    <ThemeContextProvider reducer={appReducers}>
      <div className="App">
        <Result />
      </div>
    </ThemeContextProvider>
  );
}

// container

import { createElement, useState } from "react";
import App from "./App";

const handleSearch = (searchTerm, timerRef, setTimerRef) => {
  if (timerRef) clearTimeout(timerRef);
  const newTimerRef = setTimeout(() => {
    console.log(searchTerm);
  }, 3000);
  setTimerRef(newTimerRef);
};
export const onSearchTermChange = ({
  setSearchTerm,
  timerRef,
  setTimerRef,
  handleSearch
}) => (event) => {
  setSearchTerm(event.target.value);
  handleSearch(event.target.value, timerRef, setTimerRef);
};

const useHook = (_props) => {
  const [searchTerm, setSearchTerm] = useState("");
  const [timerRef, setTimerRef] = useState();
  return {
    searchTerm,
    onSearchTermChange: onSearchTermChange({
      setSearchTerm,
      timerRef,
      setTimerRef,
      handleSearch
    })
  };
};

export default (props) => {
  const newProps = useHook(props);
  return createElement(App, { ...props, ...newProps });
};


// rootreducer
import counterReducer from "./reducers/counterReducer";
import randomReducer from "./reducers/randomReducer";

const combineReducers = (reducers) => {
  return (state, action) => {
    return Object.keys(reducers).reduce((acc, prop) => {
      return {
        ...acc,
        ...reducers[prop]({ [prop]: acc[prop] }, action)
      };
    }, state);
  };
};

export const appReducers = combineReducers({
  counter: counterReducer,
  random: randomReducer
});

// context

import { createContext, useReducer, useState } from "react";

const initialState = {
  random: { value: 0 },
  count: 0 ,
}

export const Context = createContext();

export default function ThemeContextProvider({ children }) {
  // const [state, dispatch] = useReducer(countReducer, initialState);
  const [state, setState] = useState(initialState);

  const value = { state, setState };
  return <Context.Provider value={value}>{children}</Context.Provider>;
}

// component
import { useContext } from "react";
import { Context } from "./../Context";

export default () => {
  const { state, setState } = useContext(Context);
  const increment = () => {
    setState(({ count }) => ({ count: count + 1 }));
  };
  const decrement = () => {
    setState(({ count }) => ({ count: count - 1 }));
  };
  return (
    <div>
      <button onClick={increment}>Increment </button>
      <button onClick={decrement}>Decrement </button>
      Count value is {state.count}{" "}
    </div>
  );
};

