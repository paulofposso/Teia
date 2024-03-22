# Use a imagem oficial do SDK do .NET Core como imagem base
FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build-env
WORKDIR /app

# Copia o csproj e restaura as dependências
COPY *.csproj ./
RUN dotnet restore

# Copia os arquivos do projeto e publica a aplicação
COPY . ./
RUN dotnet publish -c Release -o out

# Gera a imagem de runtime
FROM mcr.microsoft.com/dotnet/aspnet:8.0
WORKDIR /app
COPY --from=build-env /app/out .

# ENTRYPOINT ["dotnet", "teia.dll"]
#Usa a porta dinamica do heroku
CMD ["sh", "-c", "ASPNETCORE_URLS=http://*:$PORT dotnet teia.dll"]

