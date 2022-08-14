import React from 'react';

const noop = () => null;

// Encapsulate the interval behavior
const useInterval = (callback, delay) => {
    const savedCallback = useRef(noop);

    useEffect(() => {
        savedCallback.current = callback;
        savedCallback.current();
    }, [callback]);

    useEffect(() => {
        const id = setInterval(savedCallback.current, delay);

        return () => clearInterval(id);
    }, [delay]);
};

export default function Header() {
    const [color, setColor] = useState("blue");

    // setColor causes a re-render of the component
    const updateColor = setColor(color === "blue" ? "red" : "blue");

    useInterval(updateColor, 2000);

    // Use the jsx to change the color instead of reaching into the dom
  return (
    <header>
      <p>This is a <span style={{ color }}>test!</span></p>
    </header>
  )
}