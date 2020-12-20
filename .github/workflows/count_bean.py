name: count_bean

on:
  schedule:
    - cron: '30 10 * * * '
  watch:
    types: [started]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        #uses: actions/checkout@v2
        run: |
         git clone -b master https://github.com/Zero-S1/JD_tools
        
      - name: 'Set up Python'
        uses: actions/setup-python@v1
        with:
          python-version: 3.7
         
      - name: 'Install requirements'
        run: pip install -r ./requirements.txt 
        
      - name: 'run count_bean' 
        run: cd JD_tools &&  python3 count_bean.py 
        env:
            JD_COOKIE: ${{ secrets.JD_COOKIE }}
            SCKEY: ${{ secrets.SCKEY }}
            #BARK: ${{ secrets.BARK }}