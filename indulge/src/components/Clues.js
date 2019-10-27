import React, { Fragment } from "react";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";

const useStyles = makeStyles(theme => ({
  container: {
    display: "flex",
    flexWrap: "wrap"
  },
  textField: {
    marginLeft: theme.spacing(1),
    marginRight: theme.spacing(1),
    marginTop: theme.spacing(1),
    width: 200
  },
  dense: {
    marginTop: 19
  },
  menu: {
    width: 200
  }
}));

export default function Clues() {
  const classes = useStyles();
  const [values, setValues] = React.useState({
    name: ""
  });

  const handleChange = name => event => {
    setValues({ ...values, [name]: event.target.value });
  };

  return (
    <Fragment>
      <TextField
        id="standard-full-width"
        label=" I spy with my little eye... a white flag with red and blue. What is
        written on it?"
        style={{ margin: 8 }}
        placeholder="Placeholder"
        helperText="Click on submit once answered all the questions"
        fullWidth
        margin="normal"
        InputLabelProps={{
          shrink: true
        }}
      />

      <TextField
        id="standard-full-width"
        label="The one painting you did not see has more meaning than it says, find the last clue!"
        style={{ margin: 8 }}
        placeholder="Placeholder"
        helperText="Click on submit once answered all the questions"
        fullWidth
        margin="normal"
        InputLabelProps={{
          shrink: true
        }}
      />
      <Button variant="contained" color="primary" className={classes.button}>
        Take Challenge
      </Button>
    </Fragment>
  );
}
