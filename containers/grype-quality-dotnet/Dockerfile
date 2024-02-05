FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:8.0-alpine@sha256:3f93439f47fea888d94e6e228d0d0de841f4122ef46f8bfd04f8bd78cbce7ddb AS build
ARG TARGETARCH
WORKDIR /src

# copy csproj and restore as distinct layers
COPY src/*.csproj .
RUN dotnet restore -a $TARGETARCH

# copy and publish app and libraries
COPY src/ .
RUN dotnet publish -a $TARGETARCH --no-restore -o /app


FROM mcr.microsoft.com/dotnet/runtime:8.0-alpine@sha256:266fac4d418fe0f6ce50fcdc4281100d5959e23e5f42c76d5bd71736fb3ef026
WORKDIR /app
COPY --from=build /app .
USER $APP_UID
ENTRYPOINT ["./dotnetapp"]

