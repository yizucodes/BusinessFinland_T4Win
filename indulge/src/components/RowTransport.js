import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import List from "@material-ui/core/List";
import ListItem from "@material-ui/core/ListItem";
import ListItemIcon from "@material-ui/core/ListItemIcon";
import ListItemText from "@material-ui/core/ListItemText";
import DirectionsWalkIcon from "@material-ui/icons/DirectionsWalk";
import DirectionsBusIcon from "@material-ui/icons/DirectionsBus";
import DirectionsCarIcon from "@material-ui/icons/DirectionsCar";
import { Typography } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
  root: {
    width: "100%",
    maxWidth: 360,
    backgroundColor: theme.palette.background.paper,
    padding: 10
  }
}));

function ListItemLink(props) {
  return <ListItem button component="a" {...props} />;
}

export default function RowTransport() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <List component="nav">
        <Typography variant="body2" color="textSecondary" component="p">
          Gain more points for being eco-friendly, more points, more rewards!
          Choose the way to reach the landmark by clicking on the icon.
        </Typography>
        <ListItem button>
          <ListItemIcon>
            <DirectionsWalkIcon />
          </ListItemIcon>
          <ListItemText primary="Walking" />
        </ListItem>

        <ListItem button>
          <ListItemIcon>
            <DirectionsBusIcon />
          </ListItemIcon>
          <ListItemText primary="Bus" />
        </ListItem>

        <ListItem button>
          <ListItemIcon>
            <DirectionsCarIcon />
          </ListItemIcon>
          <ListItemText primary="Car" />
        </ListItem>
      </List>
    </div>
  );
}
