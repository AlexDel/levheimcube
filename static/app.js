const {
  colors,
  CssBaseline,
  ThemeProvider,
  Typography,
  Container,
  createTheme,
  Box,
  SvgIcon,
  Link,
  TextField,
  AppBar,
  Toolbar,
  IconButton,
  MenuIcon,
  Paper,
  Slider,
  Button
} = MaterialUI;


// Create a theme instance.
const theme = createTheme({
  palette: {
    primary: {
      main: '#556cd6',
    },
    secondary: {
      main: '#19857b',
    },
    error: {
      main: colors.red.A400,
    },
  },
});

function DenseAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }} style={{marginBottom: 40}}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <Typography variant="h6" color="inherit" component="div">
            Levheim Cube Predictor
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}


function App() {
  const [value, setValue] = React.useState('Controlled');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const marks = [
    {
      value: -5,
      label: 'Shame',
    },   
    {
      value: 5,
      label: 'Excitement',
    },
  ];

  const marks2 = [
    {
      value: -5,
      label: 'Anger',
    },   
    {
      value: 5,
      label: 'Disgust',
    },
  ];

  const marks3 = [
    {
      value: -5,
      label: 'Distress',
    },   
    {
      value: 5,
      label: 'Enjoyment',
    },
  ];

  const marks4 = [
    {
      value: -5,
      label: 'Fear',
    },   
    {
      value: 5,
      label: 'Surprise',
    },
  ];

  function valuetext(value) {
    return `${value}`;
  }

  return (
    <div style={{background: "#cccc", height: '100vh'}}>
      <DenseAppBar/>
      <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 5, width: '80%' },
      }}
      noValidate
      autoComplete="off"
    >
      <div style={{maxWidth: 700, margin: '0 auto'}}>
        <Paper>
          <TextField
            id="standard-multiline-static"
            label="Enter the text (Only Russian is supported)"
            multiline
            rows={10}           
            variant="standard"
          />
          <TextField id="standard-basic" label="Enter code" variant="standard" />
          <Button variant="contained" style={{display: 'block', margin: '0 auto'}}>Analyze</Button>     
          <div style={{padding: 40}}>          
            <Slider
              track={false}
              aria-labelledby="track-false-slider"           
              defaultValue={0}
              getAriaValueText={valuetext}
              marks={marks}
              min={-5}
              max={5}       
            />
            <Slider
              track={false}
              aria-labelledby="track-false-slider"           
              defaultValue={0}
              getAriaValueText={valuetext}
              marks={marks2}
              min={-5}
              max={5}       
            />
            <Slider
              track={false}
              aria-labelledby="track-false-slider"           
              defaultValue={0}
              getAriaValueText={valuetext}
              marks={marks3}
              min={-5}
              max={5}       
            />
            <Slider
              track={false}
              aria-labelledby="track-false-slider"           
              defaultValue={0}
              getAriaValueText={valuetext}
              marks={marks4}
              min={-5}
              max={5}       
            />
          </div>
        </Paper>        
      </div>
    </Box>
    </div>
  );
}

ReactDOM.render(
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>,
  document.querySelector('#root'),
);