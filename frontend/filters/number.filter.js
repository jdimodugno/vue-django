
const number = (value, float, special) => {
    if (float && special) return `${parseFloat(value).toFixed(float)} ${special}`
    else if (float) return `${parseFloat(value).toFixed(float)}`
    return value
}

export default number;
