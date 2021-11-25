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
  const diagonalValues = ['shame_excitement', 'disgust_rage', 'fear_surprise', 'enjoyment_distress'];  

  const initialState = diagonalValues.reduce((acc, entry) => ({...acc, [entry]: 0}), {});

  const [sliderValues, setSliderValues] = React.useState(initialState);

  const marks = {
    'shame_excitement':  [{value: -5, label: 'Shame'}, {value: 0, label: '|'}, {value: 5, label: 'Excitement'}],
    'disgust_rage': [{value: -5, label: 'Anger'}, {value: 0, label: '|'}, {value: 5, label: 'Disgust'}],
    'fear_surprise': [{value: -5, label: 'Distress'}, {value: 0, label: '|'}, {value: 5, label: 'Enjoyment'}],
    'enjoyment_distress': [{value: -5, label: 'Fear'}, {value: 0, label: '|'}, {value: 5, label: 'Surprise'}]
  }

  function valuetext(value) {
    return `${value}`;
  }

  function getPredictions(text, code){

  }

  function changeValue() {
    setSliderValues({...sliderValues, shame_excitement: 4})
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
          <Button variant="contained" style={{display: 'block', margin: '0 auto'}} onClick={changeValue}>Analyze</Button>     
          <div style={{padding: 40}}>
            {diagonalValues.map(diagonal =>
              <Slider   
                track={false}           
                aria-labelledby="track-false-slider"           
                value={sliderValues[diagonal]}
                getAriaValueText={valuetext}
                marks={marks[diagonal]}
                min={-5}
                max={5}
                disabled
              />
            )}        
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