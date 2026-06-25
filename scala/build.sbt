name := "app-gimnasio-multilenguaje"
version := "1.0"
scalaVersion := "2.13.12"

libraryDependencies ++= Seq(
  "com.typesafe.play" %% "play-json" % "2.9.4",
  "org.scala-lang.modules" %% "scala-parser-combinators" % "2.3.0"
)

assembly / mainClass := Some("app.Main")
assembly / assemblyJarName := "gimnasio.jar"
assembly / assemblyMergeStrategy := {
  case "module-info.class" => MergeStrategy.discard
  case x =>
    val old = (assembly / assemblyMergeStrategy).value
    old(x)
}