@echo off
REM 
python -m venv venv

REM 
call venv\Scripts\activate

REM 
pip install -r requirements.txt

echo.
echo Configuração concluída! O ambiente virtual foi criado e os pacotes foram instalados.
echo Mantenha esta janela aberta para continuar trabalhando com o ambiente ativado.
pause